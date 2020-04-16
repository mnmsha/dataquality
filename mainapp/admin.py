from django.contrib import admin
from .models import Dataquality
from .models import Choices, Popularuty_m

admin.site.register(Dataquality)
admin.site.register(Choices)
admin.site.register(Popularuty_m)
