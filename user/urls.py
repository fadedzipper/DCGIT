from django.urls import path,include,re_path
from rest_framework.routers import  SimpleRouter
from .views import UserModelViewSet

router = SimpleRouter()
router.register('users',UserModelViewSet)


urlpatterns = [
   ] + router.urls
