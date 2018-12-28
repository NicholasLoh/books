from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('auth/', include('social_django.urls', namespace='social')),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit/<int:item_id>', views.edit, name='edit'),
    path('inquiry', views.inquiry, name='inquiry'),
]
