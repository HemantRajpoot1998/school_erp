from django.db import models

# Create your models here.
# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("principal", "Principal"),
        ("teacher", "Teacher"),
        ("student", "Student"),
        ("parent", "Parent"),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
