from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from project.models import Project
from project.serializers import ProjectCreateSerializer, ProjectDetailSerializer


class ProjectViewset(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "create":
            return ProjectCreateSerializer
        return ProjectDetailSerializer
