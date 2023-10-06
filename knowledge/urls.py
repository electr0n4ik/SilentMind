from django.urls import path

from knowledge.apps import KnowledgeConfig
from rest_framework.routers import DefaultRouter

from knowledge import views

app_name = KnowledgeConfig.name

router = DefaultRouter()
router.register(r'courses', views.CourseViewSet, basename='courses')

urlpatterns = [
    path('lesson/create/', views.LessonCreateAPIView.as_view(), name='lesson-create'),
    path('lesson/', views.LessonListAPIView.as_view(), name='lesson-list'),
    path('lesson/<int:pk>/', views.LessonRetrieveAPIView.as_view(), name='lesson-once'),
    path('lesson/update/<int:pk>/', views.LessonUpdateAPIView.as_view(), name='lesson-upd'),
    path('lesson/dalete/<int:pk>/', views.LessonDestroyAPIView.as_view(), name='lesson-del'),

] + router.urls
