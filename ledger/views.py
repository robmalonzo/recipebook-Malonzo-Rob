from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Recipe

# Create your views here.

class MasterList(ListView):
    model = Recipe 
    template_name = 'master_list.html'

class Solo(DetailView):
    model = Recipe 
    template_name = 'solo.html'

def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {'recipes': recipes}
    return render(request, "ledger/master_list.html", ctx)

def recipe_detail(request, pk):
    ctx = {'recipe ': Recipe.objects.get(pk=pk)}
    return render(request, "ledger/solo.html", ctx)
