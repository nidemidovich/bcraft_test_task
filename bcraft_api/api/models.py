from django.db import models


class Statistics(models.Model):
    date = models.DateField()
    views = models.IntegerField(blank=True, null=True)
    clicks = models.IntegerField(blank=True, null=True)
    cost = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
