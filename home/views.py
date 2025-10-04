from django.shortcuts import render
from rest_framework import viewsets

from .models import Course
from .serializers import CourseSerializer
# Create your views here.
from .filters import CourseFilter


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filterset_class = CourseFilter
    search_fields = ['title', 'keywords']

