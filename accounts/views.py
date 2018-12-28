from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import UserProfileForm, UserChangeForm, EditItemForm, InquiryForm
from .models import Profile, Inquiry
from items.models import Item
from decorater import user_is_creator
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

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


@login_required
def inquiry(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        item_id = request.POST['item_id']
        item = request.POST['item']
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        message = request.POST['message']
        userId = request.POST['userId']
        sellerEmail = request.POST['sellerEmail']
        #  Check if user has made inquiry already
        user_id = request.user.id
        has_contacted = Inquiry.objects.all().filter(item_id=item_id, userId=user_id)
        if has_contacted:
            messages.error(request, 'You have already made an inquiry for this item')
            return redirect('/' + item_id)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your request has been submitted, please check your email for the reply of the seller')
        
            #Send email
            send_mail(
            'Foon Yew Text Book Inquiry',
            'There has been an inquiry for ' + item + '.'
            'Inquiry Person email: ' + email + ''
            'Person contact: ' + contact + '.'
            'Notes: ' + message + '.',
            'nicholas.lohlk@gmail.com',
            [sellerEmail],
            fail_silently=False
            )
            return redirect('/' + item_id)

    return redirect('/' + item_id)
