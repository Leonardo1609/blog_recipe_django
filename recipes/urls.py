from django.urls import path

from . import views

app_name = 'recipes'

urlpatterns = [
    path('recipes/add', views.AddRecipeView.as_view() , name='add_recipe'),
    path('recipes/', views.users_recipes_view, name='users_recipes'),
    path('recipes/<int:page>/', views.users_recipes_view, name='users_recipes'),
]
