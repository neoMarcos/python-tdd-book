from django.shortcuts import redirect, render
#from django.http import HttpResponse
from lists.models import Item, List

# Create your views here.
def home_page(request):
##    if request.method == 'POST':
##        return HttpResponse(request.POST['item_text'])
##        Item.objects.create(text=request.POST['item_text'])
##        return redirect('/lists/the-only-list-in-the-world/')
##    else:
##        new_item_text = ''

##    item.text = request.POST.get('item_text', '')
##    item.save()
##    items = Item.objects.all()
    return render(request, 'home.html')

def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})

def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/the-only-list-in-the-world/')
