from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_main_page, name='home'),
    path('cryptoprojects', views.cryptoprojects_page, name='cryptoprojects')
]
