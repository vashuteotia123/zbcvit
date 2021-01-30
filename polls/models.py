import datetime

from django.db import models
from django.utils import timezone

from app1.models import User,Event
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    # instead of showwind "True/False" in this def, it showing icon and also provide filtering 
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.ManyToManyField(User,related_name='vote_usr',blank=True)

    def __str__(self):
        return self.choice_text
