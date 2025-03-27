from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from project.models import Contributor, Project
from project.serializers import ContributorSerializer, ProjectCreateSerializer, ProjectDetailSerializer


class ProjectViewset(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "create":
            return ProjectCreateSerializer
        return ProjectDetailSerializer


class ContributorViewset(viewsets.ModelViewSet):
    queryset = Contributor.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ContributorSerializer

    def get_queryset(self):
        user = self.request.user
        return Contributor.objects.filter(project__author=user)
