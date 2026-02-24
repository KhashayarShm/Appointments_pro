from django.urls import path
from .views import TimeSlotListView, AppointmentCreateView, AppointmentListView


urlpatterns = [
    path("timeslots/", TimeSlotListView.as_view()),
    path("", AppointmentCreateView.as_view()),
    path("list/", AppointmentListView.as_view()),

]