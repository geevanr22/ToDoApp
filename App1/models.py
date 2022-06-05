from django.db import models

# Create your models here.

class ToDoApp(models.Model):

    input_date = models.DateTimeField()
    items = models.CharField(max_length=200)

    class Meta:

        verbose_name_plural = 'To Do App'
