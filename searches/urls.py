from django.urls import path
from .views import SearchAPI,SearchesAPI, AnswerAPI, AnswersAPI, SearchDeleteAPI


urlpatterns = [
    path('searches/', SearchesAPI),
    path('search/<int:search_id>/', SearchAPI),
    path('answers/', AnswersAPI),
    path('answer/<int:search_id>/<int:answer_id>/', AnswerAPI),
    path('search/delete/<int:search_id>/', SearchDeleteAPI)
]
