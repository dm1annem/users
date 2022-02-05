from django.db import models
from django.contrib.auth.models import AbstractUser

# Расширяем Пользователя своими настройками
class User(AbstractUser):
    name = models.CharField('Имя', max_length=50, blank=True)
    email = models.EmailField('Почта', unique=True, max_length=255,)
    password = models.CharField(max_length=255)
    tel = models.CharField('Телефон', max_length=16, blank=True, null=True)
    first_name = models.CharField('Отчество', blank=True, max_length=150,)
    last_name = models.CharField('Фамилия', blank=True, max_length=150,)
    is_client = models.BooleanField('Заказчик', default=False, )
    is_prorab = models.BooleanField('Прораб', default=False, )
    username = None


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
