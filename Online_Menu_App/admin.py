from django.contrib import admin
from .models import * 

admin.site.register(Users)
admin.site.register(MenuItem)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Review)
