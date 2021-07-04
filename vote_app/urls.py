from django.urls import path

from .views import VotingPage

app_name = "vote_app"
urlpatterns = [
    path("", VotingPage.as_view(), name="vote")
]
