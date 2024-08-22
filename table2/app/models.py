from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)
    fee = models.DecimalField(max_digits=10, decimal_places=2)


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.TextField()
    date_of_join = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

