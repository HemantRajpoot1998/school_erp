from django.db import models
from courses.models import ClassRoom
from accounts.models import User

# Create your models here.
class StudentProfile(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={'role': 'student'})
    assigned_class = models.ForeignKey(ClassRoom, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.student.username