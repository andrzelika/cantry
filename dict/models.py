from django.db import models

# Create your models here.
class Dictionary(models.Model):
    code = models.PositiveSmallIntegerField(default=1000)
    thing = models.CharField(max_length=100)
    definition = models.TextField()
    example = models.TextField()

    def __str__(self):
        return self.thing

class Links(models.Model):
    code = models.PositiveSmallIntegerField(default=1000)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=500)
    description = models.TextField()

    def __str__(self):
        return str(self.code)+" " + self.name
