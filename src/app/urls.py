from django.urls import path
from .views import *

urlpatterns = [
    path('',Home,name="home"),
    path('candidate/<int:pk>/',Candidate,name="candidate"),
    path('candidate-list',CandidateList,name="candidate_list"),
]