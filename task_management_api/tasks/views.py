from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import PermissionDenied
from rest_framework import permissions, viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from .models import Task, User
from .serializers import TaskSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing users.
    Allows CRUD operations on users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class TaskViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing tasks.
    Includes CRUD operations, filtering, sorting, and user ownership restrictions.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    # Add filtering and sorting capabilities
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['status', 'priority', 'due_date']  # Fields to filter by
    ordering_fields = ['due_date', 'priority']  # Fields to sort by

    def perform_create(self, serializer):
        """
        Override the default create method to associate the task
        with the currently logged-in user.
        """
        serializer.save(user=self.request.user)

    def get_queryset(self):
        """
        Restrict tasks to the logged-in user's tasks only.
        """
        return self.queryset.filter(user=self.request.user)

    def perform_update(self, serializer):
        """
        Prevent users from updating tasks they don't own.
        """
        task = self.get_object()
        if task.user != self.request.user:
            raise PermissionDenied("You do not have permission to edit this task.")
        serializer.save()


# Add a simple health check API endpoint
@api_view(['GET'])
@permission_classes([AllowAny])
def health_check(request):
    """
    Simple endpoint to check if the API is running.
    """
    return Response({"message": "API is running successfully."}, status=HTTP_200_OK)
