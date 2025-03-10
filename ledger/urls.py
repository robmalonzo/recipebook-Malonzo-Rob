from django.urls import path
from .views import RecipeDetailView, RecipeListView, index

urlpatterns = [
    path('', index, name='index'),
    path('recipes/list', RecipeListView.as_view(), name='recipes_list'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe_detail')
]

app_name = 'ledger'