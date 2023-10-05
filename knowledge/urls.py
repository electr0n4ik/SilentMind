from django.urls import path

from knowledge.apps import KnowledgeConfig
from rest_framework.routers import DefaultRouter

from knowledge.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView

app_name = KnowledgeConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-once'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson-upd'),
    path('lesson/dalete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson-del'),

] + router.urls
