from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .models import TimeSlot, Appointments
from .serializers import TimeSlotSerializer, AppointmentSerializer 
# Create your views here.



class TimeSlotListView(ListAPIView):

    serializer_class = TimeSlotSerializer
    permission_classes = [AllowAny]


    def get_queryset(self):

        business_id=self.request.query_params.get("business_id")
        date = self.request.query_params.get("date")
        qs = TimeSlot.objects.filter(is_availble=True)

        if business_id:

            qs = qs.filter(business_id=business_id)
        
        if date:

            qs = qs.filter(date=date)
        

        return qs
    
class AppointmentCreateView(CreateAPIView):

    serializer_class = AppointmentSerializer
    permission_classes = [AllowAny]

    def create(self,request,*args , **kwargs):
        data = request.data

        TimeSlot.objects.filter(
            business_id=data["business"],
            date=data["date"],
            start_time=data["start_time"]
        ).update(is_available=False)

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        appointments=serializer.save(statuse="pending")

        return Response({
            'success' : True,
            "appointment_id": appointments.id
        })


class  AppointmentListView(ListAPIView):

     serializer_class = AppointmentSerializer
     permission_classes = [IsAuthenticated]


     def get_queryset(self):

        business_id=self.request.query_params.get("business_id")
        date = self.request.query_params.get("date")
        return Appointments.objects.filter(business_owner=self.request.user,business_id=business_id)