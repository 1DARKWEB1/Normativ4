from rest_framework import serializers
from .models import Course, Subject


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ["id", "title", "description", "image"]


class CourseSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ["id", "title", "keywords", "description", "image", "slug", "subjects"]
