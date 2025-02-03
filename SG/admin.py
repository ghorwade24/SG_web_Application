from django.contrib import admin
from .models import Order,MenuCard,EnquriForFranchasi,Contact

# Register your models here.

admin.site.register(Order)
admin.site.register(EnquriForFranchasi)
admin.site.register(Contact)
@admin.register(MenuCard)
class MenuCardAdmin(admin.ModelAdmin):
    list_display = ('dish_name', 'price', 'image')
