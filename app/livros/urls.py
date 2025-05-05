from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LivroViewSet

router = DefaultRouter()
router.register(r'livros', LivroViewSet)

urlpatterns = [
    path('', include(router.urls)),  
]