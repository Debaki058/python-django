
from django.urls import path

from . import views

urlpatterns = [
    path('index', views.test_view, name= 'index'),
    path('home', views.test_view1, name='home'),
    path('form', views.form_view, name='form'),
    path('edit/<pk>', views.edit_item,name='edit'),
    path('delete/<pk>', views.delete_item,name='delete')   

]