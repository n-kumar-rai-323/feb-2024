from django.db import models

# Create your models here.



class ClassRoom(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
class Student(models.Model):
    name = models.CharField(max_length=50)
    profile_picture = models.FileField(upload_to="profile_pictures", null=True, blank=True)
    age = models.IntegerField()
    department = models.CharField(max_length=20)
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE, related_name='classroom_students', null=True, blank=True)

    def __str__(self):
        return self.name


class StudentProfile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    address = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=14)
    email = models.EmailField()

class Blood(models.Model):
    student= models.OneToOneField(Student, on_delete=models.CASCADE)
    Elligible =models.CharField(max_length=20)
    bloodgroop= models.CharField(max_length=5)
