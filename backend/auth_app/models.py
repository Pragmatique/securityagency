from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.


class User(AbstractUser):
    username = models.CharField(max_length=50, verbose_name="Пользователь")
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    father_name = models.CharField(max_length=50, verbose_name="Отчество")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=250, verbose_name="Отдел")
    position = models.CharField(max_length=250, verbose_name="Должность")
    phone = models.CharField(max_length=20, verbose_name="Телефон")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'father_name', 'last_name', 'department', 'position', 'phone']

    def __str__(self):
        return "{}".format(self.email)

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile',
                                verbose_name="Пользователь")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    city = models.CharField(max_length=50, verbose_name="Город")
    photo = models.ImageField(blank=True, verbose_name="Фото")
