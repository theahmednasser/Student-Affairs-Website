from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('search',views.search , name='search'),
    path('Department',views.Department , name='Department'),
    path('add',views.add  , name="add"),
    path('Edit',views.Edit , name='Edit'),
    path('ViewAll',views.ViewAll , name='ViewAll'),
]