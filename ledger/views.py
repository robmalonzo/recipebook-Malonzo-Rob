from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models

# Create your views here.


def index(request):
    return HttpResponse("Landing page")


class RecipeListView(ListView):
    model = models.Recipe
    template_name = 'recipes_list.html'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = models.Recipe
    template_name = 'recipes_view.html'