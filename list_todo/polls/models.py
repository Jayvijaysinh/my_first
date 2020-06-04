import datetime
from django.db import models

class todo(models.Model):
    added_date = models.DateTimeField()
    text = models.CharField(max_length=200)
