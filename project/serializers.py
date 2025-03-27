from rest_framework import serializers

from .models import Contributor, Project


class ProjectCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("name", "description", "project_type")

    def create(self, validated_data):
        user = self.context["request"].user
        project = Project.objects.create(author=user, **validated_data)

        # Add the author to the contributor
        Contributor.objects.create(user=user, project=project)

        return project


class ProjectDetailSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    contributors = serializers.StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = "__all__"
