from __future__ import unicode_literals

from django.db import models
from simple_history.models import HistoricalRecords

# Create your models here.

class MyModelWithHistory(models.Model): 
    value = models.CharField(max_length=30)
    history = HistoricalRecords()