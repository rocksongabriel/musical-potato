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

    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # TODO - email the admins the issue, or send them an sms or something of the sort
            form.save()
            return render(request, template_name="pages/complaint-submitted.html")
        return render(request, self.template_name, {"form": form})

