from django.db import models

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=150)
    email = models.CharField(max_length=250)
    subject = models.CharField(max_length=550)
    message = models.TextField(null=True)

    def __str__(self):
        return self.name