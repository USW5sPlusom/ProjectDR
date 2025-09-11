from django.db import models


class Table(models.Model):
    name = models.CharField(max_length=50, default = '', verbose_name='Заголовок')
    contant = models.TextField(default='', verbose_name='Текст')
    number = models.FloatField(default='', verbose_name='Какое то число')
    datep = models.DateField(default='datetime.date.today', verbose_name='Дата')
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-datep']
