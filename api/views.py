# api/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
import datetime
from rest_framework import generics
from .models import AppFieldUser
from .serializers import AppFieldUserSerializer

@api_view(['GET'])
def hello_world(request):
    """
    Simple hello world endpoint
    """
    return Response({
        'message': 'Hello, World!',
        'timestamp': datetime.datetime.now().isoformat(),
        'method': request.method
    })

@api_view(['GET'])
def api_status(request):
    """
    API status endpoint
    """
    return Response({
        'status': 'active',
        'version': '1.0.0',
        'endpoints': [
            '/api/hello/',
            '/api/status/',
        ]
    })

# Example class-based views for CRUD operations
class AppFieldUserListCreateView(generics.ListCreateAPIView):
    queryset = AppFieldUser.objects.all()
    serializer_class = AppFieldUserSerializer

class AppFieldUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AppFieldUser.objects.all()
    serializer_class = AppFieldUserSerializer

# Example ViewSet
# from rest_framework.viewsets import ModelViewSet

# class ItemViewSet(ModelViewSet):
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer