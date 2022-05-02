from django.urls import path
from .views import ClassifyView

urlpatterns = [
    path('classify-image/', ClassifyView.as_view(), name = 'prediction'),
]