from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Category, Candidate


class VotingPage(TemplateView):
    """view for the voting page"""
    template_name = "vote/vote-page.html"

    def get(self, request):
        context = {
            "categories": Category.objects.all(),
        }
        return render(request, self.template_name, context)


class ResultsPage(TemplateView):
    """view for the results"""
    template_name = "vote/results-page.html"
    