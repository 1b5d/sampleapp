from django.db import models, connection
from django.contrib.sites.models import Site


class SampleSite(Site):
    """
    A proxy model to extend the functionality of the Site model
    """
    class Meta:
        proxy = True

    @property
    def sum_a(self):
        """
        :return float:
        """
        return sum(o.a_value for o in self.values.all())

    @property
    def sum_b(self):
        """
        :return float:
        """
        return sum(o.b_value for o in self.values.all())

    @property
    def avg_a(self):
        """
        :return float:
        """
        count = self.values.count()
        if not count:
            return 0
        return self.sum_a / count

    @property
    def avg_b(self):
        """
        :return float:
        """
        count = self.values.count()
        if not count:
            return 0
        return self.sum_b / count

    def _aggregate_sql(self, func, attr):
        """
        Applies the aggregation function `func` to the attribute `attr` using raw SQL

        :param str func:
        :param str attr:
        :return float:
        """
        with connection.cursor() as cursor:
            cursor.execute(
                'SELECT {func}({attr}) FROM sampleapp_value WHERE site_id = %s'.format(
                    func=func, attr=attr), [self.pk])
            row = cursor.fetchone()
        return row[0] if len(row) else None

    @property
    def sql_sum_a(self):
        """
        :return float:
        """
        return self._aggregate_sql('SUM', 'a_value')

    @property
    def sql_sum_b(self):
        """
        :return float:
        """
        return self._aggregate_sql('SUM', 'b_value')

    @property
    def sql_avg_a(self):
        """
        :return float:
        """
        return self._aggregate_sql('AVG', 'a_value')

    @property
    def sql_avg_b(self):
        """
        :return float:
        """
        return self._aggregate_sql('AVG', 'b_value')


class Value(models.Model):
    """
    A model that stores the `A` and `B` values and link them to Site.
    """
    a_value = models.FloatField(null=False)
    b_value = models.FloatField(null=False)

    date_changed = models.DateTimeField(auto_now=True, null=False)
    date_created = models.DateTimeField(auto_now_add=True, null=False)

    site = models.ForeignKey(SampleSite, on_delete=models.CASCADE, related_name='values')
