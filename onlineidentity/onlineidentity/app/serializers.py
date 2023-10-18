from rest_framework import serializers
from .models import User, StudentProfile
from rest_framework.serializers import SerializerMethodField
from .utils import Utils
import random


class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        exclude = ['user', ]


class UserSerializer(serializers.ModelSerializer):
    student_profile = StudentProfileSerializer()

    class Meta:
        model = User
        fields = (
            'id', 'email', 'password', 'name', 'phone_number', 'is_student', 'is_superuser', 'student_profile',
            'is_staff', 'picture',
            'last_login',)
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            },

            'is_student': {
                'read_only': True,
            },
            'is_superuser': {
                'read_only': True,
            },
            'is_staff': {
                'read_only': True,
            },

        }

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            remove = set(fields)
            # existing = set(self.fields)
            for field_name in remove:
                self.fields.pop(field_name)

    def create(self, validated_data):
        """Create and return new user"""
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        if Utils.validate(validated_data.get('password')) == 1:
            instance.set_password(validated_data.get('password', instance.password))
        instance.save()
        return instance


class StudentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        exclude = ['user', 'student_id']


class StudentRegistrationSerializer(serializers.ModelSerializer):
    profile = StudentUserSerializer(required=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'phone_number', 'name', 'profile',)
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            },
        }

    def create(self, validated_data):
        validated_data['is_student'] = True
        profile = validated_data.pop('profile')
        user = User.objects.create_user(**validated_data)
        # student_id = self.create_new_ref_number()
        StudentProfile.objects.create(
            user=user,
            # student_id=student_id,
            year=profile['year'],
        )
        return user

    # def create_new_ref_number(self):
    #     unique_id = random.randint(10000000, 99999999)
    #     while StudentProfile.objects.filter(student_id=unique_id):
    #         unique_id = random.randint(10000000, 99999999)
    #     return unique_id
