from rest_framework import serializers
from .models import TimeSlot, Appointments


class TimeSlotSerializer(serializers.ModelSerializer):

    class Meta:
        model = TimeSlot
        fields = "__all__"

class AppointmentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Appointments
        fields = "__all__"
        read_only_fields = ("status","created_at")
