from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import UserProfileForm, UserChangeForm, EditItemForm
from .models import Profile
from items.models import Item
from decorater import user_is_creator


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        form = UserProfileForm(request.POST, request.FILES)

        # check password match
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                    return redirect('register')
                else:
                    # Looks good
                    user = User.objects.create_user(
                        username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    if form.is_valid():
                        profile = form.save(commit=False)
                        profile.user = user
                        form.save()
                    messages.success(
                        request, 'You are now registered and can log in')
                    return redirect('login')
        # password not match
        else:
            messages.error(request, 'Password not match')
            return redirect('register')

    return render(request, 'registration/register.html', {'form': UserProfileForm})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')

    return render(request, 'registration/login.html')


def logout(request):
    auth.logout(request)
    messages.success(request, 'Logged Out')
    return redirect('login')


def dashboard(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        picForm = UserProfileForm(request.POST, request.FILES)
        if 'pic' in request.POST:
            # picture validation and upload
            if picForm.is_valid():
                user = request.user
                user.profile.delete()
                profile = picForm.save(commit=False)
                profile.user = user
                picForm.save()
                return redirect('dashboard')
        elif 'edit' in request.POST:
            # edit validation and upload
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            if User.objects.filter(email=email).exists():
                messages.error(request, 'That email is being used')
                return redirect('dashboard')
            else:
                if form.is_valid():
                    form.save()
    user = request.user
    users = User.objects.all().select_related('profile')
    item = Item.objects.all().filter(user=user)
    context = {
        'items': item,
        'users': users,
        'form': UserChangeForm(request.POST, instance=request.user),
        'picForm': UserProfileForm(request.POST, request.FILES),
    }
    return render(request, 'accounts/dashboard.html', context)


def change_pass(request):
    passForm = PasswordChangeForm(request.user, request.POST)
    if request.method == 'POST':
        if passForm.is_valid():
            passForm.save()
            update_session_auth_hash(request, passForm.user)
            return redirect('logout')
    context = {
        'passForm': passForm,
    }
    return render(request, 'registration/changepass.html', context)


@user_is_creator
def edit(request, item_id):

    if request.method == 'POST':

        form = EditItemForm(request.POST, request.FILES)

        if 'edit' in request.POST:
            title = request.POST['title']
            description = request.POST['description']
            stream = request.POST['stream']
            price = request.POST['price']
            if form.is_valid():
                user = request.user
                u = Item.objects.get(pk=item_id)
                u.delete()
                item = form.save(commit=False)
                item.user = user
                form.save()
                return redirect('dashboard')

        elif 'delete' in request.POST:
            delete_item = Item.objects.get(pk=item_id)
            delete_item.delete()
            return redirect('dashboard')
    else:
        print('invalid')
    user = request.user
    item = get_object_or_404(Item, pk=item_id)
    context = {
        'form': EditItemForm(request.POST, request.FILES),
        'items': item,
        'user': user,
    }
    return render(request, 'accounts/edititem.html', context)
