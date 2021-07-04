from django.urls import path

from .views import ResultsPage, VotingPage

app_name = "vote_app"
urlpatterns = [
    path("new-vote/", VotingPage.as_view(), name="vote"),
    path("results/", ResultsPage.as_view(), name="results"),
]
