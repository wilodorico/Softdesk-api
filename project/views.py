from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from project.models import Comment, Contributor, Issue, Project
from project.permissions import IsOwnerOrReadOnly
from project.serializers import (
    CommentSerializer,
    ContributorSerializer,
    IssueSerializer,
    ProjectCreateSerializer,
    ProjectDetailSerializer,
)


class ProjectViewset(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [IsOwnerOrReadOnly]

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


class IssueViewset(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = IssueSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)


class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)
