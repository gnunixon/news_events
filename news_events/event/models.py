from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название события')
    childrens = models.ManyToManyField('self', verbose_name='Возможные следствия', blank=True, null=True)

    def __str__(self):
        return self.name
