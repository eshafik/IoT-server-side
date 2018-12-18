from django.db import models
from django.utils import timezone

# Create your models here.

class Line(models.Model):
    line_no = models.IntegerField(unique=True)

class Production(models.Model):
    line = models.ForeignKey(Line,on_delete=models.CASCADE,related_name="production")
    production_size = models.IntegerField()
    production_date = models.DateTimeField(default=timezone.now)