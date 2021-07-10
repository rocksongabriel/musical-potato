from django.contrib.auth import get_user_model
from django.db.models import fields
from django.forms import inlineformset_factory
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.base import TemplateView

from .models import Candidate, Category

User = get_user_model()
from django.contrib.auth.mixins import LoginRequiredMixin


class VotingCategoriesListPage(LoginRequiredMixin, TemplateView):
    """view for displaying the various categories to vote in"""
    template_name = "vote/voting-categories-list.html"
    model = Category
    context_object_name = "categories"

    def get(self, request, *args, **kwargs):
        voter = request.user
        context = {
            "categories": self.model.objects.all().exclude(voters=voter), # remove the categories the voter has already voted in
            "user": request.user
        }
        if context["categories"].count() > 0:
            return render(request, self.template_name, context)
        else:
            return render(request, template_name="vote/voting-completed.html")

    # TODO - if remove the categories the voter has voted in from the displayed categories


class VotingPage(LoginRequiredMixin, TemplateView):
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

        # Get the upvote key
        for key in request.POST.keys():
            if 'upvote' in key:
                # Get the full name from the key
                full_name = " ".join([name.capitalize() for name in key.split("_")[1].split("-")])
        # Get the candidate using the full name
        candidate = Candidate.objects.get(full_name=full_name)
        # Upvote the candidate 
        candidate.upvote()

        # Get the user and add him to the voters of the category
        voter = request.user
        
        # Add the voter to the category's voters
        category.voters.add(voter)

        # Check the forms validity and save it
        if formset.is_valid():
            formset.save()
        return HttpResponseRedirect(self.success_url)

        # TODO - handle error if a voter doesn't vote for anybody and tries to submit
        # TODO - do not allow the voter for in a category twice

    def get(self, request, slug):
        category = Category.objects.get(slug=slug)
        
        # Check if the user has voted in the category already and redirect him if he has
        user = request.user
        if user.username in [voter.username for voter in category.voters.filter(username__search=user.username)]:
            return render(request, template_name="vote/already-voted.html", context={"user": user})

        formset = self.CandidateInlineFormset(instance=category)
        context = {"category": category, "formset": formset}
        return render(request, self.template_name, context)


class ResultsPage(TemplateView):
    """view for the results"""
    template_name = "vote/results-page.html"