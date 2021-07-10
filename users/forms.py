from django import forms

from django.contrib.auth import get_user, get_user_model


class SignupForm(forms.ModelForm):
    """Form to create a user account"""

    class Meta:
        model = get_user_model()
        fields = ["username", "password"]