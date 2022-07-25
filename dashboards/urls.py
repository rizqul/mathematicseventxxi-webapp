from django import urls
from django.urls import path

from .views import (
    AboutView,
    DocumentView,
    Home,
    IndexView,
    TutorialRegistrasiView,
    DataView,

)

app_name = 'dashboards'
urlpatterns = [
    path('dashboards/<user_id>', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('document/', DocumentView.as_view(), name='document'),
    path('data/', DataView.as_view(), name='data'),
    path('tutorial/', TutorialRegistrasiView.as_view(), name='tutorial'),
    path('', Home.as_view(), name='home'),
]
