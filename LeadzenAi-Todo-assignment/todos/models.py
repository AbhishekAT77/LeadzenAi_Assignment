from django.db import models

# Create your models here.

#The task model contains the fields[Content,data,complete ] "ID" will be primary key generated automatically by Django ORM
class Task(models.Model):
    content = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.content}'

    class Meta:
        ordering = ['-date_created']
