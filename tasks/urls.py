from django.contrib import admin
from django.urls import path,include

from . import views


urlpatterns = [
    path('', views.task, name='task'),
    path('task_det<int:task_id>',views.task_details,name='Task_det')
]
