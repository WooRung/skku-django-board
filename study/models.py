from django.db import models


# Create your models here.


class Score(models.Model):
    student = models.ForeignKey('Students', on_delete=models.CASCADE)
    english = models.CharField(max_length=10)
    math = models.CharField(max_length=10)
    science = models.CharField(max_length=10)
    exam_date = models.DateField(null=True, )


class Students(models.Model):
    name = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    email = models.CharField(max_length=30)


class StudentClassroom(models.Model):
    student = models.ForeignKey("Students", on_delete=models.CASCADE)
    classroom = models.ForeignKey("Classroom", on_delete=models.CASCADE)
    reg_date = models.DateTimeField(auto_now_add=True, auto_now=True)

class Classroom(models.Model):
    name = models.CharField(max_length=50)
    student_set = models.ManyToManyField("Students", through="StudentClassroom")



# Students.objects.get(id=1).student_classroom_set[0].classroom_set
# Students.objects.get(id=1).prefetch_related('classroom_set').classroom_set