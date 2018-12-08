from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from .forms import AddForm
# Create your views here.
def home(request):
    item = Item.objects.all()
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
    return render(request, 'search.html')

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