from rest_framework import serializers

from knowledge.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    """Для модели курса добавьте в сериализатор поле вывода количества уроков."""
    lesson = LessonSerializer(source='lesson_set', many=True)

    class Meta:
        model = Course
        fields = '__all__'
