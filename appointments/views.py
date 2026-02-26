from rest_framework.generics import ListAPIView, CreateAPIView,UpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .models import TimeSlot, Appointment, Customer
from .serializers import * 
from .models import TimeSlot
from business.models import Services
from .serializers import TimeSlotSerializer
import datetime
from datetime import timedelta
class TimeSlotCreateView(CreateAPIView):
    serializer_class = TimeSlotSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = request.data

        service = Services.objects.get(id=data["service"])
        duration = service.duration

        start_time = datetime.strptime(data["start_time"], "%H:%M").time()
        end_time = (datetime.combine(datetime.today(), start_time) + timedelta(minutes=duration)).time()

        slot = TimeSlot.objects.create(
            business=service.business,
            service=service,
            date=data["date"],
            start_time=start_time,
            end_time=end_time,
            is_available=True
        )

        return Response({
            "success": True,
            "slot_id": slot.id,
            "start_time": slot.start_time,
            "end_time": slot.end_time
        })

    
class AppointmentCreateView(CreateAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        data = request.data

        slot = TimeSlot.objects.get(id=data["slot"], is_available=True)

        customer, created = Customer.objects.get_or_create( 
            business=slot.business, 
            phone=data["customer_phone"], 
            defaults={"name": data["customer_name"]} 
            )

        slot.is_available = False
        slot.save()

        appointment = Appointment.objects.create(
            business=slot.business,
            service=slot.service,
            slot=slot,
            customer_name=data["customer_name"],
            customer_phone=data["customer_phone"],
            status="pending"
        )

        return Response({
            "success": True,
            "appointment_id": appointment.id
        })



class AppointmentStatusUpdateView(UpdateAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Appointment.objects.filter(business__owner=self.request.user)

    def update(self, request, *args, **kwargs):
        appointment = self.get_object()
        new_status = request.data.get("status")

        if new_status not in ["pending", "confirmed", "canceled"]:
            return Response({"error": "Invalid status"}, status=400)

        appointment.status = new_status
        appointment.save()

        return Response({"success": True, "status": appointment.status})



class  AppointmentListView(ListAPIView):

     serializer_class = AppointmentSerializer
     permission_classes = [IsAuthenticated]


     def get_queryset(self):

        business_id=self.request.query_params.get("business_id")
        date = self.request.query_params.get("date")
        return Appointments.objects.filter(business_owner=self.request.user,business_id=business_id)
     



class TimeSlotListView(ListAPIView):
    serializer_class = TimeSlotSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        business_id = self.request.query_params.get("business_id")
        service_id = self.request.query_params.get("service_id")
        date = self.request.query_params.get("date")

        qs = TimeSlot.objects.filter(is_available=True)

        if business_id:
            qs = qs.filter(business_id=business_id)

        if service_id:
            qs = qs.filter(service_id=service_id)

        if date:
            qs = qs.filter(date=date)

        return qs



class CustomerListView(ListAPIView):
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Appointment.objects.filter(
            business__owner=self.request.user
        ).values("customer_name", "customer_phone").distinct()
