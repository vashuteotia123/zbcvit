import datetime

from django.db import models
from django.utils import timezone

from app1.models import User,Event
class Task(models.Model):
    task_img=models.ImageField(upload_to="task_photos/",null=True)
    task_category=models.CharField(max_length=200)
    task_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    task_description=models.CharField(max_length=5000)
    subs = models.ManyToManyField(User, related_name='subs', blank=True)

    def __str__(self):
        return self.task_text


class video_links(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    link = models.CharField(max_length=200)



    def __str__(self):
        return self.link

class documents_links(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.link