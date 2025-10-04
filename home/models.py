from django.db import models


# Create your models here.
from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="courses/")
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Subject(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="subjects")
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="subjects/", blank=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.course.title})"

