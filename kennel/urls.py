from django.urls import path
from .views import KennelView

urlpatterns = [
    path('home', KennelView.as_view())
]