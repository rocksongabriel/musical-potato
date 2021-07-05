from django.db.models import fields
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from .models import Category, Candidate
from django.forms import inlineformset_factory


class VotingCategoriesListPage(ListView):
    """view for displaying the various categories to vote in"""
    template_name = "vote/voting-categories-list.html"
    model = Category
    context_object_name = "categories"


class VotingPage(TemplateView):
    """view for the voting page"""
    template_name = "vote/vote-page.html"

    CandidateInlineFormset = inlineformset_factory(Category,
                                                   Candidate,
                                                   fields=(
                                                       "full_name",
                                                       "picture",
                                                       "upvote",
                                                   ),
                                                   extra=0,
                                                   can_delete=False)

    def post(self, request, slug):
        category = Category.objects.get(slug=slug)
        formset = self.CandidateInlineFormset(request.POST,
                                              request.FILES,
                                              instance=category)
        context = {"category": category}
        if formset.is_valid():
            formset.save()
        return render(request, self.template_name, context)

    def get(self, request, slug):
        category = Category.objects.get(slug=slug)
        formset = self.CandidateInlineFormset(instance=category)
        context = {"category": category, "formset": formset}
        return render(request, self.template_name, context)


class ResultsPage(TemplateView):
    """view for the results"""
    template_name = "vote/results-page.html"
