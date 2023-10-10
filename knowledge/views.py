from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics, status
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from knowledge.models import Course, Lesson, Payment, CourseSubscription
from knowledge.paginators import MyPagination
from knowledge.permissions import IsOwnerOrStaff
from knowledge.serializers import CourseSerializer, LessonSerializer, \
    PaymentSerializer  # , CourseSubscriptionSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """ViewSet для работы с моделью."""
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = MyPagination

    # permission_classes = [IsAuthenticated]  # доступ для авторизованных пользователей
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user'] = self.request.user
        return context

    def list(self, request, *args, **kwargs):
        # Получите список курсов
        queryset = self.get_queryset()
        serializer = CourseSerializer(queryset, many=True, context={'request': request})

        # Пройдитесь по каждому курсу и добавьте статус подписки
        for course_data in serializer.data:
            course = Course.objects.get(pk=course_data['id'])
            user = request.user
            is_subscribed = CourseSubscription.objects.filter(user=user, course=course).exists()
            course_data['is_subscribed'] = is_subscribed

        return Response(serializer.data)

    def sub(self, request, pk=None):
        # Установка подписки пользователя на курс
        course = self.get_object()
        user = request.user

        # Проверяем, не подписан ли пользователь уже на этот курс
        if CourseSubscription.objects.filter(user=user, course=course).exists():
            return Response({"detail": "User is already subscribed to this course"}, status=status.HTTP_400_BAD_REQUEST)

        subscription = CourseSubscription(user=user, course=course)
        subscription.save()
        return Response({"detail": "Subscription created"}, status=status.HTTP_201_CREATED)

    def unsub(self, request, pk=None):
        # Удаление подписки пользователя на курс
        course = self.get_object()
        user = request.user

        try:
            subscription = CourseSubscription.objects.get(user=user, course=course)
        except CourseSubscription.DoesNotExist:
            return Response({"detail": "User is not subscribed to this course"}, status=status.HTTP_400_BAD_REQUEST)

        subscription.delete()
        return Response({"detail": "Subscription deleted"}, status=status.HTTP_204_NO_CONTENT)


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()  # .order_by('-id')
    permission_classes = [IsOwnerOrStaff]
    # pagination_class = MyPagination


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwnerOrStaff]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course', 'lesson', 'method_pay')
    ordering_fields = ('data_pay',)

    def perform_create(self, serializer):
        new_payment = serializer.save()
        new_payment.owner = self.request.user
        new_payment.save()


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer

# class CourseSubscriptionCreateAPIView(generics.CreateAPIView):
#     serializer_class = CourseSubscriptionSerializer
#     permission_classes = [IsAuthenticated]
#
#     def perform_create(self, serializer):
#         new_sub = serializer.save()
#         new_sub.owner = self.request.course
#         new_sub.save()
#
#
# class CourseSubscriptionDestroyAPIView(generics.DestroyAPIView):
#     queryset = CourseSubscription.objects.all()
