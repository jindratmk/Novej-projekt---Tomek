from django.urls import path

from . import views

urlpatterns = [
    path('', views.models_list),
    path('as', views.test_list, name='test_list')

]
