from django.shortcuts import render,HttpResponse,redirect
from items.models import Item,Category
from .forms import SignupForm
from demo.settings import send_mail
import os
from dotenv import load_dotenv
def index(request):
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()

    return render(request,'core/index.html',{
                  'categories':categories,
                  'items':items,
                  })
subject = 'test'
def contact(request):
    query_name = request.POST.get('name')
    query_email = request.POST.get('email')
    query_text = request.POST.get('text')
    send_mail(
    "support", 
    f"From: {query_email}\n\n{query_text}", # ტექსტში ჩაამატე იუზერის მეილი
    os.getenv("EMAIL_HOST_USER"),           # From: შენი მეილი
    [os.getenv("EMAIL_HOST_USER")],
    fail_silently=False        # To: შენი მეილი (სიის სახით!)
)
    return render(request,'core/contact.html')

def all_items(request):
    #Variable query gets id of category clicked
    query = request.GET.get('category')
    categories = Category.objects.all()
    #if query exists, filter items by category id, else show all items
    if query:
        items = Item.objects.filter(category_id=query)
    else:
        items = Item.objects.all()
    #Render the all_items.html template with the items and categories
    return render(request, 'core/all_items.html', {
        'items': items,
        'categories': categories,
    })

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

def about_us(request):
    return render(request,'core/about_us.html')


def search(request):
    #pulls user inputed name from request user sent by html input tag
    #This Query is sent by an user
    query = request.GET.get('item')
    
    if query:
        items = Item.objects.filter(name__icontains=query)
    
        return render(request, 'core/all_items.html', {
            'items': items,
        
        })
    else:
        items = Item.objects.all()
        return render(request, 'core/all_items.html', {
            'items': items,
        
        })