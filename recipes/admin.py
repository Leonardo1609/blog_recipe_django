from django.contrib import admin

from .models import Recipe
# Register your models here.

class RecipeAdmin(admin.ModelAdmin):
    fields = ('title', 'category', 'author', 'image', 'preparation', 'ingredients')

admin.site.register(Recipe, RecipeAdmin)
