from django.db import models

# Create your models here.
class CustomerDetail(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    contact_number = models.CharField(max_length=10)
    City = models.CharField(max_length=30)

    # def __str__(self):
    #    return f"{self.id} {self.first_name} {self.last_name} {self.City}"