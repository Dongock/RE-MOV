from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.conf import settings


class UserManager(BaseUserManager):
    def create_user(self, username, nickname, email, gender, date_of_birth, password=None):
        if not email:
            raise ValueError('Users must have an email address')
     
        user = self.model(
            username = username,
            email=self.normalize_email(email),
            nickname = nickname,
            gender = gender,
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, nickname, gender, date_of_birth, password):
        user = self.create_user(
            username = username,
            email = email,
            nickname = nickname,
            gender = gender,
            date_of_birth=date_of_birth,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    

class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=12, unique = True)
    nickname = models.CharField(max_length=12, unique = True)
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    followers=models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='followings'
        )


    objects = UserManager()

    REQUIRED_FIELDS = ['email', 'nickname','date_of_birth', 'gender']
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin