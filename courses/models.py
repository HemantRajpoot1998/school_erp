from django.db import models
from accounts.models import User

# Create your models here.
# ✅ Course Model
class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

# ✅ Class Model
class ClassRoom(models.Model):
    name = models.CharField(max_length=50)  # Example: "Class 10A"
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                limit_choices_to={'role': 'teacher'})

    def __str__(self):
        return f"{self.name} - {self.course.name}"