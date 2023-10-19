from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError
import random


# Create your models here.


class UserManager(BaseUserManager):
    """Manager  for base User"""

    def create_user(self, email, password=None, **extra_fields):
        """Create a new user"""
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password, **extra_fields):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, password, name=name, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.is_student = True
        user.save(using=self._db)
        return user


def file_size_image(value):  # add this to some file where you can import it from
    limit = 1.5 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('Image too large. Size should not exceed 1.5 MiB.')


class User(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(null=True, max_length=20)
    address = models.CharField(max_length=100, null=True)
    passport = models.CharField(max_length=20, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_student = models.BooleanField(default=True)
    date_modified = models.DateTimeField(auto_now=True)
    picture = models.ImageField(upload_to='data/profile_image/%Y/%m',
                                default='place-holder.jpg', blank=True, null=True, validators=[file_size_image])
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', ]

    def get_full_name(self):
        """Retrieve full name for user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of user"""
        return self.email


#
# class Course(models.Model):
#     """Programmes under a faculty"""
#     name = models.CharField(max_length=100, unique=True)
#
#     def __str__(self):
#         return self.name
#
def create_new_ref_number():
    unique_id = random.randint(10000000, 99999999)
    while StudentProfile.objects.filter(student_id=unique_id):
        unique_id = random.randint(10000000, 99999999)
    return unique_id


class StudentProfile(models.Model):
    """User Profile for student extra information"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student_profile")
    student_id = models.IntegerField(default=create_new_ref_number)
    # course = models.ForeignKey(Course, on_delete=models.PROTECT, related_name='course')
    year = models.IntegerField()
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        """TO set the table name in database"""
        db_table = "student_profile"

    def __str__(self):
        return self.user.name
