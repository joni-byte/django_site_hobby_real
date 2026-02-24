from django.shortcuts import render, get_object_or_404, redirect
from items.models import Item 
from django.contrib import messages 
from .models import CartItem # შემოიტანე ახალი მოდელი

def cart_summary(request):
    if request.user.is_authenticated:
        # ვიღებთ ნივთებს ბაზიდან კონკრეტული იუზერისთვის
        db_items = CartItem.objects.filter(user=request.user).select_related('item')
        cart_items = [ci.item for ci in db_items]
    else:
        # თუ იუზერი არ არის შესული, ვაჩვენებთ ცარიელ კალათას
        messages.warning(request, "Please log in to see your cart.")
        cart_items = []
    
    return render(request, 'cart/cart_summary.html', {
        'cart_items': cart_items
    })

def add_to_cart(request, pk):
    # კალათა ბაზაში მხოლოდ ავტორიზებული იუზერებისთვის მუშაობს
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in to add items to cart.")
        return redirect('myapp:login')

    item = get_object_or_404(Item, pk=pk)
    
    # ვამოწმებთ, უკვე არის თუ არა ეს ნივთი ამ იუზერის კალათაში
    already_exists = CartItem.objects.filter(user=request.user, item=item).exists()
    
    if already_exists:
        messages.info(request, "This item is already in your cart!")
    else:
        # ვინახავთ ბაზაში - ეს დარჩება სამუდამოდ
        CartItem.objects.create(user=request.user, item=item)
        messages.success(request, "Item added to cart successfully!")
        
    return redirect('cart:cart_summary')

def remove_from_cart(request,pk):
    item = get_object_or_404(Item, pk=pk)

    is_in_cart = CartItem.objects.filter(user=request.user, item=item).exists()

    if is_in_cart:

        cart_item = CartItem.objects.get(user=request.user, item=item)

        cart_item.delete()

        messages.success(request, "Item was sucesfully deleted from cart")
    else:
        messages.warning(request,"This item is not in cart")
    return redirect('cart:cart_summary')
