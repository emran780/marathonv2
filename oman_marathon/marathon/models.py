from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Runner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biography = models.TextField(blank=True, null=True)
    healthy_condition = models.CharField(max_length=255, blank=True, null=True)
    nationality = models.CharField(max_length=255, blank=True, null=True)
    chosen_run = models.CharField(max_length=50, choices=[('5K', '5K'), ('10K', '10K'), ('Kids', 'Kids')], blank=True, null=True)

    def __str__(self):
        return self.user.username

class ContactUsMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.email}"
    


    
    
