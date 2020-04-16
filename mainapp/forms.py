from django import forms
from .models import Dataquality
from .models import Popularuty_m

class dataqualityform(forms.ModelForm):
    class Meta:
        model = Dataquality
        fields = ('file', 'source', 'full_classificators')

class assesment(forms.ModelForm):
    class Meta:
        model = Popularuty_m
        fields = ("popularuty_1",)
