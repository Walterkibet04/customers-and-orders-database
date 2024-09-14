from django.urls import path, include
from .views import CustomerViewSet

# urlpatterns = [
#     path('register/', CustomerViewSet.as_view(), name="register")
# ]
from rest_framework import routers
from .views import CustomerViewSet, OrderViewSet


router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = router.urls
