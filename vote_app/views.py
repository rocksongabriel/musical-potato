from django.db.models import fields
from django.forms import inlineformset_factory
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.base import TemplateView

from .models import Candidate, Category


class VotingCategoriesListPage(ListView):
    """view for displaying the various categories to vote in"""
    template_name = "vote/voting-categories-list.html"
    model = Category
    context_object_name = "categories"


class VotingPage(TemplateView):
    """view for the voting page"""
    template_name = "vote/vote-page.html"
    success_url = reverse_lazy("vote_app:vote-categories")

    CandidateInlineFormset = inlineformset_factory(Category,
                                                   Candidate,
                                                   fields=(
                                                       "full_name",
                                                       "picture",
                                                   ),
                                                   extra=0,
                                                   can_delete=False)

    def post(self, request, slug):
        category = Category.objects.get(slug=slug)
        formset = self.CandidateInlineFormset(request.POST,
                                              request.FILES,
                                              instance=category)

        # Get the upvote key from the request dict
        # Get the candidate full name from the key
        # Fetch the candidate object using the full name
        # Increase the candidates number of votes

        # Get the upvote key
        for key in request.POST.keys():
            if 'upvote' in key:
                # Get the full name from the key
                full_name = " ".join([name.capitalize() for name in key.split("_")[1].split("-")])
                print(full_name)
        # Get the candidate using the full name
        candidate = Candidate.objects.get(full_name=full_name)
        # Upvote the candidate 
        candidate.upvote()

        # Check the forms validity and save it
        if formset.is_valid():
            formset.save()
        return HttpResponseRedirect(self.success_url)

    def get(self, request, slug):
        category = Category.objects.get(slug=slug)
        formset = self.CandidateInlineFormset(instance=category)
        context = {"category": category, "formset": formset}
        return render(request, self.template_name, context)


class ResultsPage(TemplateView):
    """view for the results"""
    template_name = "vote/results-page.html"
