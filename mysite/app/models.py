from django.db import models

# Create your models here.

class Report(models.Model):
    DEFAULT = 50
    id = models.IntegerField(primary_key=False)
    uwnetid = models.CharField(max_length = DEFAULT, null=True, default=None, blank=True)
    first_name = models.CharField(max_length=DEFAULT, null=True, default=None, blank=True)
    last_name = models.CharField(max_length=DEFAULT, null=True, default=None, blank=True)
    case_type = models.CharField(max_length=DEFAULT, null=True, default=None, blank=True)
    date = models.CharField(max_length=DEFAULT, null=True, default=None, blank=True)
    description = models.CharField(max_length=DEFAULT, null=True, default=None, blank=True)
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

    def __str__(self):
        return self.uwnetid if self.uwnetid else 'Anonymous'

    def compare(this, other):
        return (this and other) and (this.casefold() == other.casefold())

    def checkMatch(self):
        allReports = Report.objects.all()
        matches = []
        for prev in allReports:
            if (compare(self.last_name, prev.last_name) and compare(self.first_name, prev.first_name)) or compare(
                    self.ig_acc, prev.ig_acc) or compare(self.phone_num, prev.phone_num):
                matches.append(prev)

        return len(matches)

    def checkMatchSimple(self):
        allReports = Report.objects.all()
        matches = []
        for prev in allReports:
            if ((self.last_name and prev.last_name) and (self.last_name.casefold() == prev.last_name.casefold())):
                matches.append(prev)

        return len(matches) - 1

    def id(self):
        return self.id

