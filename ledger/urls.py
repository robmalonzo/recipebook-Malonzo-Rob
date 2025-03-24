from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('recipes/list', views.RecipeListView.as_view(), name='recipes_list'),
    path('recipe/<int:pk>', views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe/add', views.RecipeCreateView.as_view(), name='recipe_add'),
]

app_name = 'ledger'