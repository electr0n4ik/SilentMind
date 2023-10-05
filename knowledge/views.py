from rest_framework import viewsets

from knowledge.models import Course
from knowledge.serializers import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """ViewSet для работы с моделью."""
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


