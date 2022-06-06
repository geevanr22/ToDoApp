from django.db import models
# from datetime import datetime, date
# Create your models here.

class ToDoApp(models.Model):

    input_date = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    items = models.CharField(max_length=200)

    class Meta:

        verbose_name_plural = 'To Do App'
