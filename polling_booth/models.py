from django.db import models
from django.utils import timezone
import datetime
# Create your models here.

class Question(models.Model):
    ques_text = models.CharField(max_length=200)
    publish_date = models.DateField('date published')

    #used for the object representation
    def __str__(self):
        return self.ques_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.publish_date <= now

class Choice(models.Model):
    # to define the relationship, ForeignKey are used
    ques = models.ForeignKey(Question,on_delete=models.CASCADE) #arguments- to class which is relatied,
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
