from decimal import Decimal
from itertools import product
from django.shortcuts import get_object_or_404, redirect, render,HttpResponse
from django.urls import reverse
from SG.models import MenuCard,EnquriForFranchasi,Contact,Order,OrderItem
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


    
# Create your views here.
def home(request):
    menu_items = MenuCard.objects.all()  # Fetch all menu items from the database
    cart = request.session.get('cart', [])  # Retrieve cart from session
    return render(request, 'Menu.html', {'menu_items': menu_items, 'cart': cart})
def menu_view(request):
    menu_items = MenuCard.objects.all()
    cart = request.session.get('cart', {})
    cart_count = sum(cart.values())  # Total number of items in the cart
    
    return render(request, 'Menu.html', {
        'menu_items': menu_items,
        'cart_count': cart_count
    })

# View to handle adding items to the cart
def add_to_cart(request, item_id):
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        
        # Increment quantity if item is already in the cart, otherwise set it to 1
        if str(item_id) in cart:
            cart[str(item_id)] += 1
        else:
            cart[str(item_id)] = 1
        
        request.session['cart'] = cart  # Update cart in session
        
        return redirect(reverse('menu_view'))  # Redirect to the menu page

# View to display items in the cart (order page)
def order_view(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = Decimal('0.00')
    
    # Retrieve items from the cart and calculate total price
    for item_id, quantity in cart.items():
        menu_item = get_object_or_404(MenuCard, pk=item_id)
        total_item_price = menu_item.price * quantity
        cart_items.append({
            'item': menu_item,
            'quantity': quantity,
            'total_price': total_item_price
        })
        total_price += total_item_price

    # Check if the user is logged in
    if request.user.is_authenticated:
        user = request.user
    else:
        user = None  # Or handle guest checkout here
    
    # Create the Order and OrderItems
    order = Order.objects.create(
        user=user,  # You can set user to None if it's a guest order
        total_price=total_price,
        status="Pending"  # You can change this status later (e.g., after payment)
    )
    
    # Create OrderItems for each item in the cart
    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            menu_item=item['item'],
            quantity=item['quantity'],
            total_price=item['total_price']
        )
    
    # Clear the cart after placing the order
    request.session['cart'] = {}

    # Render the order confirmation page
    return render(request, 'order.html', {
        
        'cart_items': cart_items,
        'total_price': total_price
    })
    

# Clear cart after placing order (optional)
def clear_cart(request):
    if 'cart' in request.session:
        del request.session['cart']
    return redirect(reverse('menu_view'))

def order(request):
    cart = request.session.get("cart", [])
    total_price = sum(item["price"] for item in cart)  # Calculate total price
    return render(request, "cartOrder.html", {"order_items": cart, "total_price": total_price})