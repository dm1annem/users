from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    is_client = models.BooleanField('Заказчик', default=False, verbose_name='Заказчик')
    is_prorab = models.BooleanField('Прораб', default=False, verbose_name='Прораб')
    Username = None

    USERNAME_FIELD = email
    REQUIRED_FIELDS = []
