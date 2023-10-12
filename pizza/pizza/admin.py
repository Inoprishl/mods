from django.contrib import admin
from .models import PizzaModel, ToppingsModel, PizzaProxy

# Register your models here.
class PizzaInline(admin.TabularInline):
    model = PizzaProxy
    extra = 0 #change amount of visible objects of m2m field
    verbose_name = 'topping(vn)'
    verbose_name_plural = 'Create new pizza recipe(vnp)'
    
class PizzaAdmin(admin.ModelAdmin):
    inlines = [
        PizzaInline,
    ]
    exclude = ('toppings', )
    list_display = ('name', 'all_toppings')

admin.site.register(PizzaModel, PizzaAdmin)
admin.site.register(ToppingsModel)