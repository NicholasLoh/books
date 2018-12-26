from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User

def seller(request, items_user_id):

    return render(request, 'home.html')