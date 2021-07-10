from django.contrib.auth import get_user_model
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls.base import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView

from .forms import SignupForm


# Login form
class UserLoginView(LoginView):
    template_name = "users/login.html"
    redirect_field_name = reverse_lazy("vote_app:vote-categories")



# class SignupView(TemplateView):
#     """View to create a user account"""
#     template_name = "users/signup.html"
#     model = get_user_model()
#     form_class = SignupForm
#     success_url = reverse_lazy("vote_app:vote-categories")

#     def get(self, request, **kwargs):
#         context = {
#             "form": self.form_class()
#         }
#         return render(request, self.template_name, context)

#     def post(self, request, **kwargs):
#         form = self.form_class(request.POST)
#         context = {
#             "form": self.form_class(initial=request.POST)
#         }
#         if form.is_valid():
#             # create user object
#             user = self.model().create_user(
#                 username=request.POST['username'],
#                 password=request.POST['password']
#             )
#             print(user)
#             # authenticate the user 
#             # log the user in 
#             # redirect to the voting page

#             print(request.POST)
#             return redirect(self.success_url)
#         return render(request, self.template_name, context)
