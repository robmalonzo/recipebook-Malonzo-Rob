from django.urls import path
from .views import MasterList, Solo

app_name = 'ledger'

urlpatterns = [
    path('recipes/list/', MasterList.as_view() , name='master_list'), 
    path('recipe/<int:pk>/', Solo.as_view(), name='recipe-detail'), 
]
