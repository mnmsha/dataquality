from django.shortcuts import render, get_object_or_404, redirect
from .forms import dataqualityform, assesment
from .models import Dataquality, Popularuty_m
from .models import Choices
from django.http import HttpResponse, HttpResponseRedirect
from .defs import availability_def, machinereadability_def, authority_def, popularuty_def, class_dict_def, reliability_def, relevance_def, fullness_def
from django.utils import timezone

def post_list(request):
    posts = Dataquality.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'mainapp/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Dataquality, pk=pk)
    if request.method == "POST":
        form = assesment(request.POST)
        Popularuty_m = form.save(commit=False)
        if form.is_valid():
            Popularuty_m.pk_Dataquality = pk
            Popularuty_m.save()
    else:
        form = assesment()
    return render(request, 'mainapp/post_detail.html', {"pk": pk, 'post': post, 'form': form})

def dataquality_new(request):
    if request.method == "POST":
        form = dataqualityform(request.POST, request.FILES)
        Dataquality = form.save(commit=False)
        if form.is_valid():
            t=list(Dataquality.__class__.objects.filter(source__startswith=Dataquality.source).values_list("pk", flat=True))
            o=0
            q=0
            for i in t:
                r=list(Popularuty_m.objects.filter(pk_Dataquality__startswith=i).values_list("popularuty_1", flat=True))
                q=q+len(r)
                o=o+sum(r)
            if q != 0:
                Dataquality.popularuty = o/q/10
            else:
                Dataquality.popularuty = o/10

            Dataquality.authority_full =float(authority_def(Dataquality.source))

            l=list(Dataquality.__class__.objects.all().values_list("authority", flat=True))
            u=0
            for i in l:
                if i != None:
                    u=u+float(i)
            if len(l) != 0:
                k=u/len(l)
                if Dataquality.authority_full < k:
                    if Dataquality.authority_full == 0:
                        Dataquality.authority == 0
                    else:
                        Dataquality.authority = k/Dataquality.authority_full
                else:
                    Dataquality.authority == 1
            else:
                Dataquality.authority == 1

            Dataquality.availability = availability_def(Dataquality.source)

            Dataquality.machinereadability = machinereadability_def(Dataquality.file)
            p=class_dict_def(Dataquality.file)
            Dataquality.relevance = reliability_def(relevance_def(p))
            Dataquality.reliability = reliability_def(p)
            Dataquality = form.save(commit=False)
            Dataquality.published_date = timezone.now()
            Dataquality.save()
            form.save_m2m()

            s=str(Dataquality.__class__.objects.earliest('-id'))
            s=s.replace('D','').replace('a','').replace('t','').replace('q','').replace('u','').replace('l','').replace('i','').replace('y','').replace('o','').replace('b','').replace('j','').replace('e','').replace('c','').replace('(','').replace(')','').replace(' ','')
            h=list(Dataquality.__class__.objects.filter(id__startswith=int(s)).values_list("full_classificators", flat=True))

            Dataquality.fullness = fullness_def(h, Dataquality.file)


            Dataquality.save()
            return redirect('post_detail', pk=Dataquality.pk)
    else:
        form = dataqualityform()
        return render(request, 'mainapp/dataquality_edit.html', {'form': form})
