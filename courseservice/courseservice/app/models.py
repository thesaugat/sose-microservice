from django.db import models


# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=75)
    code = models.CharField(max_length=10)
    credit = models.IntegerField(default=6)

    def __str__(self):
        return self.title


class CourseEnrollment(models.Model):
    trimester_choices = (
        ('spring', 'SPRING'),
        ('fall', 'FALL'),

    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student_id = models.IntegerField()
    session = models.IntegerField()
    trimester = models.CharField(choices=trimester_choices, max_length=10)

    def __str__(self):
        return str(self.student_id)

    class Meta:
        unique_together = ('course', 'student_id')
