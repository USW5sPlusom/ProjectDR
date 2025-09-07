from django.db import models


class Table(models.Model):
    name = models.CharField(max_length=50, default = '')
    contant = models.TextField(default='')
    number = models.FloatField(default='')
    date = models.DateField(default='datetime.date.today')
