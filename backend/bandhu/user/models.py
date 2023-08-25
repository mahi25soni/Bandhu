from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=400)
    date = models.DateField(default= timezone.now)


class Sentiments(models.Model) :
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    percent = models.IntegerField()
