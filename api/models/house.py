from django.db import models
from .school import School

# Create your models here.
class House(models.Model):
    name = models.CharField(max_length=100)
    total_capacity = models.IntegerField(default=0)
    number_of_students = models.IntegerField(default=0)
    school = models.ForeignKey(School, related_name='houses', on_delete=models.CASCADE)

    def __str__(self):
        return self.name