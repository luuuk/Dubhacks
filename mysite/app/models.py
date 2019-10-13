from django.db import models

# Create your models here.

class Report(models.Model):
    DEFAULT = 30
    uwnetid = models.CharField(max_length = DEFAULT)

