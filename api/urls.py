# api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router for ViewSets (optional)
router = DefaultRouter()
# router.register(r'items', views.ItemViewSet)  # Example ViewSet

urlpatterns = [
    # Include router URLs (for ViewSets)
    path('', include(router.urls)),
    
    # Custom API endpoints
    path('hello/', views.hello_world, name='hello_world'),
    path('status/', views.api_status, name='api_status'),
    path('app_field_user/', views.AppFieldUserListCreateView.as_view(), name='app_field_user_list_create'),
    path('app_field_user/<int:pk>/', views.AppFieldUserDetailView.as_view(), name='app_field_user_detail'),
]