from django.db import models


# Create your models here.


class City(models.Model):
    City_Name = models.CharField(max_length=30)

    def __str__(self):
        return self.City_Name


class Course(models.Model):
    Course_Name = models.CharField(max_length=30)

    def __str__(self):
        return self.Course_Name


class StudentDB(models.Model):
    Name = models.CharField(max_length=45)
    Age = models.IntegerField()
    Phno = models.BigIntegerField()
    City_Name = models.ForeignKey(City, on_delete=models.CASCADE)
    Course_Name = models.ForeignKey(Course, on_delete=models.CASCADE)


# class login(models.Model):
#     Userid = models.CharField(max_length=30)
#     Password = models.BigIntegerField()
