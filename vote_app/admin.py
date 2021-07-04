from django.contrib import admin
from .models import Candidate, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ["full_name", "category", "number_of_votes"]