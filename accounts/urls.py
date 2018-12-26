from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    #path('login/', views.login, name='login'),
    #path('logout/', views.logout, name='logout'),
    path('auth/', include('social_django.urls', namespace='social')),
    #path('change_pass/', views.change_pass, name='change_pass'),
    #path('change-password/', views.change_pass, name='change_pass'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit/<int:item_id>', views.edit, name='edit'),
]
