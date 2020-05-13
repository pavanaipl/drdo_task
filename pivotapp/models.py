from django.db import models

# Create your models here.

class UsersDetails(models.Model):


    name = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    mobile_number = models.CharField(max_length=11, null=True, blank=True)
    age = models.IntegerField(default=0)
    dob = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

