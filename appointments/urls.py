from django.urls import path
from .views import CustomerListView,TimeSlotListView, AppointmentCreateView, AppointmentListView


urlpatterns = [
    path("timeslots/", TimeSlotListView.as_view()),
    path("", AppointmentCreateView.as_view()),
    path("list/", AppointmentListView.as_view()),
    path("customers/", CustomerListView.as_view()),

]