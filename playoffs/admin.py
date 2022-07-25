from django.contrib import admin

# Register your models here.
from .models import(
    PlayOffPenyisihan,
    PlayOffSemifinal,
)
admin.site.register(PlayOffPenyisihan)
admin.site.register(PlayOffSemifinal)