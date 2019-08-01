from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.conf import settings

# Create your models here.
class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)



class User(AbstractUser):
    #username = models.CharField(max_length=50, verbose_name="Пользователь")
    username = None
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    father_name = models.CharField(max_length=50, verbose_name="Отчество")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=250, verbose_name="Отдел")
    position = models.CharField(max_length=250, verbose_name="Должность")
    phone = models.CharField(max_length=20, verbose_name="Телефон")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'father_name', 'last_name', 'department', 'position', 'phone']
    objects = UserManager()

    def __str__(self):
        return "{}".format(self.email)

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile',
                                verbose_name="Пользователь")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    city = models.CharField(max_length=50, verbose_name="Город")
    photo = models.ImageField(blank=True, verbose_name="Фото", null=True)
