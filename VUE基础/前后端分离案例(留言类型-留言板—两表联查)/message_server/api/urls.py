from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('cate', views.CateView)
router.register('message', views.MessageView)

urlpatterns = router.urls