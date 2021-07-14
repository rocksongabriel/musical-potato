from django.shortcuts import render
from django.views.generic import TemplateView
from vote_app.forms import SupportForm


class HomePage(TemplateView):
    template_name = "pages/homepage.html"
    form_class = SupportForm
    

    def get(self, request, **kwargs):
        context = {
            "form": self.form_class()
        }
        return render(request, self.template_name, context)