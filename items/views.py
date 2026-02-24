from django.shortcuts import render, get_object_or_404
from items.models import Item,Category 

def detail(request,pk):
    items = get_object_or_404(Item, pk=pk)
    return render(request,'item/detail.html',{
        'item':items
    })

from django.shortcuts import render, get_object_or_404, redirect # Add redirect

def cart(request, pk):
    item = get_object_or_404(Item, pk=pk)
    cart = request.session.get('cart_items', [])
    
    if pk not in cart:
        cart.append(pk)
        request.session['cart_items'] = cart
        # Mark the session as modified so Django knows to save it
        request.session.modified = True 
    
    # Instead of rendering, redirect to the summary page
    return redirect('item:cart_summary')
def cart_summary(request):
    # Get the IDs from the session
    item_ids = request.session.get('cart_items', [])
    
    # Fetch the actual Item objects from the database using those IDs
    cart_items = Item.objects.filter(pk__in=item_ids)
    
    return render(request, 'item/cart_summary.html', {
        'cart_items': cart_items
    })