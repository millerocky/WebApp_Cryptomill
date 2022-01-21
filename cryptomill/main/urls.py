from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_main_page, name='home'),
    path('crypto', views.cryptoprojects_page, name='crypto'),
]
