from knowledge.apps import KnowledgeConfig
from rest_framework.routers import DefaultRouter

from knowledge.views import CourseViewSet

app_name = KnowledgeConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [

] + router.urls
