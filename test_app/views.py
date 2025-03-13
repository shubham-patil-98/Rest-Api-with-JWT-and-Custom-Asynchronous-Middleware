from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Task
from django.http import JsonResponse
from .serializers import TaskSerializer
from .pagination import MyPageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = MyPageNumberPagination
    permission_classes = [IsAuthenticated]

@api_view(['GET'])  # Specify allowed HTTP methods
@authentication_classes([JWTAuthentication])  # Enforce JWT authentication
@permission_classes([IsAuthenticated])  # Only authenticated users can access this
def external_data_view(request):
    # Access the data added by the middleware
    if hasattr(request, 'external_api_data') and request.external_api_data:
        return JsonResponse(request.external_api_data, safe=False)
    else:
        return JsonResponse({"error": "No data available"}, status=404)
