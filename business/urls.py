from django.urls import path
from .views import *


urlspatterns=[
    path("client/",BusinessListCreateView.as_view()),
    path("client/<int:pk>/",BusinessDetailView.as_view()),
    path("",ServiceListCreateView.as_view()),
    path("<int:pk>/", ServiceDetailView.as_view()),
]
