from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.utils.translation import gettext_lazy as _


# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(max_length=30, unique=True)
#     email = models.EmailField(_('email address'), unique=True)
#     first_name = models.CharField(_('first name'), max_length=30, blank=True)
#     last_name = models.CharField(_('last name'), max_length=30, blank=True)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     date_joined = models.DateTimeField(default=timezone.now)
#     birth_date = models.DateField(null=True, blank=True)
#
#     objects = UserManager() # использование стандартного менеджера пользователей
#
#     USERNAME_FIELD = 'username'	# какое поле будет использоваться в качестве уникального идентификатора
#     REQUIRED_FIELDS = ['email', 'birth_date']	# список полей, которые должны быть обязательными при создании суперпользователя
#
#     def __str__(self):
#         return self.email


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    established_date = models.DateField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'library_book_from_first_app'  # Задаем имя таблицы в базе данных
        ordering = ['-published_date']  # Сортировка по убыванию даты публикации
        verbose_name = 'fiction book'  # Человекочитаемое имя модели
        verbose_name_plural = 'fiction books'  # Человекочитаемое множественное число имени модели
        unique_together = ('title', 'author')  # Уникальность по комбинации полей title и author
        index_together = ('title', 'author')  # Создание индексов по полям title и author
        get_latest_by = 'published_date' # Поле для определения последней записи в таблице
        indexes = [
           models.Index(fields=['title', 'author']),
           models.Index(fields=['published_date'], name='published_idx'),
        ] # Создание различных индексов


    def __str__(self):
        return self.title

