from django.contrib import admin
from .models import Food, Category,HeroSection

admin.site.register(Food)
admin.site.register(Category)
admin.site.register(HeroSection)



from django.contrib import admin
from .models import CategoryMenu, SubCategory, FoodMenu

class SubCategoryInline(admin.TabularInline):
    model = SubCategory
    extra = 1

class CategoryMenuAdmin(admin.ModelAdmin):
    inlines = [SubCategoryInline]

class FoodMenuAdmin(admin.ModelAdmin):
    list_display = ("name", "categoryMenu", "subcategory", "price", "is_available")
    list_filter = ("categoryMenu", "subcategory")

admin.site.register(CategoryMenu, CategoryMenuAdmin)
admin.site.register(SubCategory)
admin.site.register(FoodMenu, FoodMenuAdmin)