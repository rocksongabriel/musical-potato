from django.contrib import admin
from .models import Candidate, Category


class CandidateInline(admin.TabularInline):
    model = Candidate
    extra = 0
    min_num = 1
    show_change_link = True

    readonly_fields = ("number_of_votes", "upvote",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [CandidateInline, ]
    list_display = ["name"]
    readonly_fields = ("slug",)


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ("full_name", "image_tag", "category", "number_of_votes",)
    readonly_fields = ("number_of_votes", "upvote",)