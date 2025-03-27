from django.db import IntegrityError
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

    def update(self, instance, validated_data):
        user = self.context["request"].user

        if instance.author != user:
            raise serializers.ValidationError("You are not authorized to update this project.")

        return super().update(instance, validated_data)


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = "__all__"

    def create(self, validated_data):
        user_authenticated = self.context["request"].user
        project = validated_data["project"]

        # Check if the user authenticated is author of the project for which they are trying to add a contributor
        if project.author != user_authenticated:
            raise serializers.ValidationError("You are not authorized to add a contributor to this project.")

        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({"user": "This user is already a contributor to this project."})
