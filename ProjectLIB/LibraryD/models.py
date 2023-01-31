from django.db import models


# Create your models here.

class Course(models.Model):
    Course_Name = models.CharField(max_length=89)

    def __str__(self):
        return f'{self.Course_Name}'


class Books(models.Model):
    Book_Name = models.CharField(max_length=89)
    Author_Name = models.CharField(max_length=89)
    Course_id = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.Book_Name}'


class Student(models.Model):
    Stud_Password = models.CharField(max_length=34)
    Stud_Name = models.CharField(max_length=69)
    Stud_Phno = models.BigIntegerField(default=0)
    Stud_Sems = models.IntegerField(default=0)
    Course_Name = models.ForeignKey(Course, on_delete=models.CASCADE)


class Issue(models.Model):
    Stud_Name = models.ForeignKey(Student, on_delete=models.CASCADE)
    Book_Name = models.ForeignKey(Books, on_delete=models.CASCADE)
    Start_Date = models.DateField()
    End_Date = models.DateField()








