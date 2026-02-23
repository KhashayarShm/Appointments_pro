from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
# Create your views here.


class BusinessListCreateView(ListCreateAPIView):

    serializer_class = BusinessSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Business.objects.filter(owner=self.request.user)
    

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BusinessDetailView(RetrieveUpdateAPIView):
    
    serializer_class = BusinessSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Business.objects.filter(owner=self.request.user)


class ServiceListCreateView(ListCreateAPIView):
    
    serializer_class = BusinessSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        Business_id = self.request.query_params.get("business_id")
        qs = Services.objects.filter(active=True)
        if business_id :
            qs = qs.filter(Business_id)
        return qs

    def perform_create(self, serializer):
        business_id = self.request.data.get("business")
        business = Business.objects.get(id=business_id,owner=self.request.user)
        serializer.save(business=business)
    

class ServiceDetailView(RetrieveUpdateAPIView):
    
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Services.objects.filter(owner=self.request.user)
