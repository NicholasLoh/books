from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('<int:item_id>', views.item, name='item'),
    path('search/', views.search, name='search'),
    path('addItem', views.addItem, name='addItem'),
]