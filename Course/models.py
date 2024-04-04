from django.db import models

# Create your models here.
class Course(models.Model):
    Name = models.CharField(max_length=50)
    Price = models.IntegerField()
    Discount = models.IntegerField()
    Duration = models.CharField(max_length=30)
    AutherName = models.CharField(max_length=100)

    def __str__(self):
        return self.Name
    
