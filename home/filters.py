from .models import Course
import django_filters


class CourseFilter(django_filters.FilterSet):
    class Meta:
        model = Course
        fields = {
            'title': ['exact', 'icontains'],  # exact - strogiy parametr    icontains - so'zda yoki gapta
            # istalgan oxwaw harf yoki sozlarni topsa olib chiqib beradi
            'slug': ['exact'],
            'id': ['exact', 'gte', 'lte']
        }