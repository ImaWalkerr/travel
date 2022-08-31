from rest_framework import routers
from src.tourism.urls import router as tourism_router
from src.users.urls import router as customer_router


router = routers.DefaultRouter()
router.registry.extend(tourism_router.registry)
router.registry.extend(customer_router.registry)
