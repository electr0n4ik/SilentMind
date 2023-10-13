import stripe
from django.conf import settings
from django.core.exceptions import FieldDoesNotExist
from rest_framework import serializers
from knowledge.models import Course, Lesson, Payment, CourseSubscription
from knowledge.validators import TitleValidator, UrlYouTubeValidator

stripe.api_key = settings.SECRET_KEY_STRIPE


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

    lesson_list = LessonSerializer(source='lesson_set', many=True, read_only=True)

    def get_lesson_count(self, obj):
        if obj.lesson_set.all():
            # return len(obj.lesson_set.all())
            return obj.lesson_set.all().count()
        return 0

    def get_is_subscribed(self, obj):
        user = self.context.get('user')
        try:
            if user.is_authenticated:
                return CourseSubscription.objects.filter(user=user, course=obj).exists()
        except:
            return False

    class Meta:
        model = Course
        fields = '__all__'


class PaymentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    data_pay = serializers.DateField()
    method_pay = serializers.CharField()
    try:
        lesson_id = serializers.IntegerField()
    except:
        course_id = serializers.IntegerField()

    class Meta:
        model = Payment
        fields = '__all__'
