from rest_framework import viewsets
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer
from rest_framework.permissions import AllowAny

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [AllowAny]

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]
