from django import *
from django.shortcuts import redirect ,render

from .models import MenuCard,EnquriForFranchasi,Contact
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def HomePage(request):
    return render(request ,'home.html')
def AboutPage(request):
    return render(request,'About-us.html')

def MenPage(request):
    # Fetch all menu items from the database
    menu_items = MenuCard.objects.all()
    return render(request, 'Menu.html', {'menu_items': menu_items})
def FranchasiPage(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        Age = request.POST.get("age")
        Mobile_Num = request.POST.get("mobile")
        email = request.POST.get("email")
        
        city = request.POST.get("city")
    
        location = request.POST.get("location")
        save_data = EnquriForFranchasi(Invester_name=name,Phone_number=Mobile_Num,Email=email,City=city,Locations_are_you_oppening=location,age = Age)
        save_data.save()
    return render(request,'Franchasi.html')
def ContactPage(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        mobile = request.POST.get("mobile")
        email = request.POST.get("email")
        feedback = request.POST.get("feedback")
        save_data= Contact(name=name,mobile=mobile,email=email,feedback=feedback)
        save_data.save()
    
    return render(request, 'Contact-us.html')

    
    
   

# def cart_add(request):
#     cart = Cart(request)
#     if request.POST.get('action')=='post':
#         item = (request.POST.get('item.dish_name'))
#         product = get_object_or_404(MenuCard,id=item)
#         cart.add(product=product)
#         cart_quantity = len(cart)
        
#         # response = JsonResponse({"Product name: ":product.dish_name})
#         response = JsonResponse({"qty: ":cart_quantity})
        
#         return response
#     else:
#         # If the request is not POST, return an empty response or handle as needed
#         return JsonResponse({"error": "Invalid request"}, status=400)
