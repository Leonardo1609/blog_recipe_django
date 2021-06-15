import math

from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.views.generic.base import TemplateView

from .models import Recipe
from .forms import RecipeForm

# Create your views here.

def users_recipes_view(request, profile_slug, page=1):
    if request.user.profile.slug != profile_slug:
        return redirect('index')
    items_per_page = 5
    recipes_list = Recipe.objects.filter(author=request.user.profile).order_by('-created_at')
    total_pages = math.ceil(recipes_list.count() / items_per_page) 

    if page > total_pages:
        return redirect( 'recipes:users_recipes', profile_slug, 2 )

    if page < 1:
        return redirect( 'recipes:users_recipes', profile_slug )

    paginator = Paginator(recipes_list, items_per_page)
    
    # 5 recipes
    page_obj = paginator.get_page(page)

    return render(request, 'users_recipes.html', { 
        'recipes': page_obj, 
        'total_pages': total_pages, 
        'page': page, 
        'previous_page': page - 1 if page > 1 else 0,
        'next_page': page + 1 if page < total_pages else total_pages
    })
    
class AddRecipeView(TemplateView):
    template_name = 'form_recipe.html'

    def post(self, request, *args, **kwargs):
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(request.user.profile)
            return redirect('recipes:users_recipes', kwargs['profile_slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe_form'] = RecipeForm(self.request.POST or None)
        return context
