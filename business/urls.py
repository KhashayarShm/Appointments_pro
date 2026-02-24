from django.urls import path
from .views import BusinessListCreateView, BusinessDetailView, ServiceListCreateView, ServiceDetailView

urlpatterns = [
    path("", BusinessListCreateView.as_view()),
    path("<int:pk>/", BusinessDetailView.as_view()),
    path("services/", ServiceListCreateView.as_view()),
    path("services/<int:pk>/", ServiceDetailView.as_view()),
]
