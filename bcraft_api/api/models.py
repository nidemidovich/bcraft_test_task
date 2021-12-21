import decimal

from django.db import models


class Statistics(models.Model):
    date = models.DateField()
    views = models.IntegerField(blank=True, null=True)
    clicks = models.IntegerField(blank=True, null=True)
    cost = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)

    @property
    def cpc(self):
        if self.cost is None and self.clicks is None:
            return None
        return round(self.cost / decimal.Decimal(str(self.clicks)), 2)

    @property
    def cpm(self):
        if self.cost is None and self.clicks is None:
            return None
        return round(decimal.Decimal(1000) * self.cost / decimal.Decimal(str(self.views)), 2)
