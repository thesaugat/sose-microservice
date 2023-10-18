from django.db import models


# Create your models here.

class Books(models.Model):
    author = models.CharField(max_length=100)
    book_name = models.CharField(max_length=250)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.book_name


class BooksBorrow(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    student_id = models.IntegerField()
    active = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('book', 'student_id', 'active')
