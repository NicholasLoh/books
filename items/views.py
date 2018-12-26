from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from .forms import AddForm
# Create your views here.
def home(request):
    item = Item.objects.order_by('list_date')
    context = {
        'items': item,
    }
    return render(request, 'home.html', context)

def item(request, item_id):
    user = request.user
    item = get_object_or_404(Item, pk = item_id)
    context = {
        'items': item,
        'user' : user,
    }
    return render(request, 'item.html', context)
    
def search(request):
    item = Item.objects.order_by('list_date')
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            item = item.filter(description__icontains = keywords)

    if 'stream' in request.GET:
        stream = request.GET['stream']
        if stream == '理科':
            item = item.exclude(stream = '文商').exclude(stream = '商')
        elif stream == '文商':
            item = item.exclude(stream = '理科').exclude(stream = '商')
        elif stream == '商':
            item = item.exclude(stream = '理科')    
    context = {
        'items' : item,
    }
    return render(request,'search.html', context)

def addItem(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        stream = request.POST['stream']
        price = request.POST['price']
        form = AddForm(request.POST, request.FILES)
        if form.is_valid(): 
            user = request.user
            item = form.save(commit=False)
            item.user = user
            form.save()
            return redirect('dashboard')
          
    context = {
        'form': AddForm(request.POST, request.FILES),
    }
    return render(request, 'add.html', context)