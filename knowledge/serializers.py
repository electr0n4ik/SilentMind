from rest_framework import serializers

from knowledge.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    """Для модели курса добавьте в сериализатор поле вывода количества уроков."""
    lesson_count = serializers.SerializerMethodField()
    # lesson = LessonSerializer(source='lesson_set', many=True)

    def get_lesson_count(self, obj):
        if obj.lesson_set.all():
            # return len(obj.lesson_set.all())
            return obj.lesson_set.all().count()
        return 0

    class Meta:
        model = Course
        fields = '__all__'
