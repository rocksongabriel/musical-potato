from django.urls import path

from .views import ResultsPage, VotingCategoriesListPage, VotingPage

app_name = "vote_app"
urlpatterns = [
    path("election-categories/", VotingCategoriesListPage.as_view(), name="vote-categories"),
    path("election-categories/<slug:slug>/add-new-vote/", VotingPage.as_view(), name="vote"),
    path("election-results/", ResultsPage.as_view(), name="results"),
]
