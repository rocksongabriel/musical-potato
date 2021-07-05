from django.urls import path

from .views import ResultsPage, VotingCategoriesListPage, VotingPage

app_name = "vote_app"
urlpatterns = [
    path("voting-list/", VotingCategoriesListPage.as_view(), name="vote-categories"),
    path("category/<slug:slug>/add-new-vote/", VotingPage.as_view(), name="vote"),
    path("results/", ResultsPage.as_view(), name="results"),
]
