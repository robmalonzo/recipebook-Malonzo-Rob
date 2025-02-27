from django.contrib import admin
from .models import Recipe, RecipeIngredient

# Register your models here.
class RecipeIngredientLine(admin.TabularInline):
    model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    inlines = [RecipeIngredientLine]

admin.site.register(Recipe, RecipeAdmin)

