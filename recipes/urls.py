from django.urls import path

from . import views

app_name = 'recipes'

urlpatterns = [
    path('admin/add', views.AddRecipeView.as_view() , name='add_recipe'),
    path('admin/', views.users_recipes_view, name='users_recipes'),
    path('admin/<int:page>/', views.users_recipes_view, name='users_recipes'),
    path('recipes/<slug:slug>', views.RecipeView.as_view(), name="recipe_detail")
]
