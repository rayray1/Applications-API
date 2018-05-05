from django.db import models


class Applist(models.Model):
    application = models.FileField(blank=False, null=False)
    package_name = models.CharField(max_length=200)
    package_version_code = models.FloatField(blank=False, null=False)
