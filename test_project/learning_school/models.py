from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserGroup(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название группы')
    students = models.ManyToManyField(User)
    product = models.ForeignKey('Product',
                                   on_delete=models.CASCADE)
    min_user_count = models.IntegerField(verbose_name='Минимальное количество учеников')
    max_user_count = models.IntegerField(verbose_name='Максимальное количество учеников')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Author(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    surname = models.CharField(max_length=50, verbose_name='Фамилия')

    def __str__(self):
        return f"{self.first_name} {self.surname}"

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название продукта')
    date = models.DateField(verbose_name='Дата')
    start_time = models.TimeField(verbose_name='Время старта')
    price = models.FloatField(verbose_name='Стоимость')
    author = models.ForeignKey(Author,
                               on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Access(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Доступ'
        verbose_name_plural = 'Доступы'


class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название урока')
    link = models.URLField(verbose_name='Ссылка')
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
