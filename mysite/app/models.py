from django.db import models

# Create your models here.

class Report(models.Model):
    DEFAULT = 50
    uwnetid = models.CharField(max_length = DEFAULT, null=True, default=None, blank=True)
    first_name = models.CharField(max_length=DEFAULT, null=True, default=None, blank=True)
    last_name = models.CharField(max_length=DEFAULT, null=True, default=None, blank=True)
    location = models.CharField(max_length=DEFAULT, null=True, default=None, blank=True)
    hair_color = models.CharField(max_length=DEFAULT, null=True, default=None, blank=True)
    eye_color = models.CharField(max_length=DEFAULT, null=True, default=None, blank=True)
    age = models.CharField(max_length=DEFAULT, null=True, default=None, blank=True)
    ethnicity = models.CharField(max_length=DEFAULT, null=True, default=None, blank=True)
    university = models.CharField(max_length=DEFAULT, null=True, default=None, blank=True)
    organization = models.CharField(max_length=DEFAULT, null=True, default=None, blank=True)
    ig_acc = models.CharField(max_length=DEFAULT, null=True, default=None, blank=True)
    fb_acc = models.CharField(max_length=DEFAULT, null=True, default=None, blank=True)
    phone_num = models.CharField(max_length=DEFAULT, null=True, default=None, blank=True)
    snap_acc = models.CharField(max_length=DEFAULT, null=True, default=None, blank=True)


