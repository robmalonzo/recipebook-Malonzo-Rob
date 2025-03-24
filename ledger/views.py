from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
from . import forms

# Create your views here.


def index(request):
    return HttpResponse("Landing page")


class RecipeListView(ListView):
    model = models.Recipe
    template_name = 'recipes_list.html'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = models.Recipe
    template_name = 'recipes_view.html'


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = models.Recipe
    form_class = forms.RecipeForm
    template_name = 'recipes_form.html'
    success_url = reverse_lazy('ledger:recipes_list')


class RecipeImageCreateView(LoginRequiredMixin, CreateView):
    model = models.RecipeImage
    form_class = forms.RecipeImageForm
    template_name = 'recipes_add_image.html'

    def form_valid(self, form):
        recipe = get_object_or_404(models.Recipe, pk=self.kwargs['pk'])
        recipe_image = form.save(commit=False)
        recipe_image.recipe = recipe
        recipe_image.save()
        return redirect('ledger:recipe_detail', pk=recipe.pk)

    def get_success_url(self):
        return reverse_lazy('ledger:recipe_detail', kwargs={'pk': self.kwargs['pk']})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe'] = get_object_or_404(models.Recipe, pk=self.kwargs['pk'])
        return context