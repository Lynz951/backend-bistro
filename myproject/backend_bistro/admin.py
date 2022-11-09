from django.contrib import admin
from .models import MenuItems, Diet, Category


# Register your models here.

class MenuItemsAdmin(admin.ModelAdmin):
    pass
admin.site.register(MenuItems, MenuItemsAdmin)

class DietAdmin(admin.ModelAdmin):
    pass
admin.site.register(Diet, DietAdmin)

class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category, CategoryAdmin)