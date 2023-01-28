"""Hillside_project URL Configuration
"""

from django.urls import path, include
from rest_framework import routers
from products.views import ProductViewSet


router = routers.DefaultRouter(trailing_slash=False)
router.register('products', ProductViewSet)

urlpatterns = router.urls
