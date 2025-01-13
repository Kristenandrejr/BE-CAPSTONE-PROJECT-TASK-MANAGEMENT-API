from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as auth_views
from .views import TaskViewSet, UserViewSet, health_check

# Initialize the DefaultRouter
router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')  # Endpoint for tasks
router.register(r'users', UserViewSet, basename='user')  # Endpoint for users

# Include the router's URLs in the urlpatterns
urlpatterns = [
    path('', include(router.urls)),  # Use 'include' to add the router's URLs
    path('token-auth/', auth_views.obtain_auth_token, name='token-auth'),  # Token authentication endpoint
    path('health/', health_check, name='health-check'),  # Health check endpoint
]
