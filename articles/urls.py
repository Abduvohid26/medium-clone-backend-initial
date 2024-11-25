from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticlesView

router = DefaultRouter()
router.register(r'articles', ArticlesView)

urlpatterns = [
    path('', include(router.urls)),
]