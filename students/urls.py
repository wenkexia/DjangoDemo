from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'stu',views.StudentModelViewSet)


urlpatterns = router.urls
