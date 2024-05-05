from django.contrib import admin
from . models import Pet, Category, Review
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',),}
    list_display = ['name', 'slug']
    
admin.site.register(Pet)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review)