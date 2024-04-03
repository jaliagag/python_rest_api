from django.urls import re_path as url
from django.urls import path, include
from .views import (
    TodoListApiView,
)

urlpatterns = [
    path('api', TodoListApiView.as_view()),
]
