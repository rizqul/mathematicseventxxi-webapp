from django.urls import path

from .views import (
    StartPenyisihanPlayoffView,
    UjianPenyisihanPlayoffView,
    StartSemifinalPlayoffView,
    UjianSemifinalPlayoffView
)

app_name = 'playoffs'
urlpatterns = [
    path('start_penyisihan/', StartPenyisihanPlayoffView.as_view(), name='start_penyisihan'),
    path('ujian_penyisihan/<exam_code>', UjianPenyisihanPlayoffView.as_view(), name='ujian_penyisihan'),
    path('start_semifinal/', StartSemifinalPlayoffView.as_view(), name='start_semifinal'),
    path('ujian_semifinal/<exam_code>', UjianSemifinalPlayoffView.as_view(), name='ujian_semifinal'),
    
]
