"""
Definition of models.
"""

from django.db import models
# Create your models here.
class registerAlt(models.Model): 
   email = models.CharField(
        max_length=20)
   password = models.CharField(
        max_length=20
    )
   password_confirmation=models.CharField(
        max_length=20
    )