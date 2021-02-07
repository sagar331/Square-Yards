# from app.views import
from . import views
from django.urls import path,include
# from rest_framework import routers import 
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'users', views.MapViewSet,basename='user')
urlpatterns = router.urls