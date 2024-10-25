from django.shortcuts import render
from django.views.generic import TemplateView
from .models import * 

class MainPage (TemplateView):
    template_name = "MainPage.html"

def All_data(request):
    users = Users.objects.all()  
    menu_items = MenuItem.objects.all() 
    orders = Order.objects.all()  
    order_items = OrderItem.objects.all()
    
    return render(request, 'MainPage.html', {
         
        'menu_items': menu_items,
         
    })  