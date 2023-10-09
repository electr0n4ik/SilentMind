from rest_framework import serializers

from knowledge.models import Course, Lesson, Payment, CourseSubscription
from knowledge.validators import TitleValidator, UrlYouTubeValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [
            TitleValidator(field='title'),
            serializers.UniqueTogetherValidator(fields=['title'], queryset=Lesson.objects.all()),
            UrlYouTubeValidator(field='url_video')
        ]


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    is_subscribed = serializers.SerializerMethodField()
    # lesson = LessonSerializer(source='lesson_set', many=True)

    def get_lesson_count(self, obj):
        if obj.lesson_set.all():
            # return len(obj.lesson_set.all())
            return obj.lesson_set.all().count()
        return 0

    def get_is_subscribed(self, obj):
        user = self.context.get('user')
        if user.is_authenticated:
            return CourseSubscription.objects.filter(user=user, course=obj).exists()
        return False

    class Meta:
        model = Course
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


# class CourseSubscriptionSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = CourseSubscription
#         fields = '__all__'
