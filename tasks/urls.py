
from django.urls import path
from .views import TodayTasks

urlpatterns = [
    path('tasks', TodayTasks.as_view(), name="today")
]