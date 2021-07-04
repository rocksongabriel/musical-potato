from django.shortcuts import render
from django.views.generic.base import TemplateView


class VotingPage(TemplateView):
    """view for the voting page"""
    template_name = "vote/vote-page.html"