from django.contrib import admin
from .models import Recipe, RecipeIngredient, RecipeImage


# Register your models here.
class RecipeIngredientLine(admin.TabularInline):
    model = RecipeIngredient


class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ("name",)
    inlines = [RecipeIngredientLine]


class RecipeImageLine(admin.TabularInline):
    model = RecipeImage


class RecipeImageAdmin(admin.ModelAdmin):
    list_display = ("name", "author", "created_on")
    inlines = [RecipeImageLine]


admin.site.register(Recipe, RecipeIngredientAdmin)
admin.site.register(RecipeImage)