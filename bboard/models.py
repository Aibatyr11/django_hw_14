from django.db import models
from django.contrib.auth.password_validation import *

from django.core.validators import *


class Crypto(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True)

    def get_absolute_url(self):
        return f"/bboard/{self.pk}"

    # для управлением данными в админе
    class Meta:
        verbose_name_plural = "Rubrics"
        verbose_name = "Rubric"
        ordering = ['name']

    def __str__(self):
        return self.name


# Create your models here.
def max_length():
    return 5


# def validate_even(val):
#     if val % 2 != 0:
#         raise ValidationError("число является нечетным", code="odd", params={"val": val})


class MinMaxValueValidator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value):
        if value < self.min_value or value > self.max_value:
            raise ValidationError(
                f"Введеное число не входит в диапазон от {self.min_value} - {self.max_value}",
                code="out_of_range",
                params={"min_value": self.min_value, "max_value": self.max_value},
            )


class Bb(models.Model):
    rubric = models.ForeignKey(Rubric, on_delete=models.PROTECT, null=True)
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)

    published = models.DateTimeField(auto_now_add=True, db_index=True)

    # title_and_price.short_description = "Данная функция объединеят цену заголовок"

    def model_func(self):
        if self.title == "sport" and self.price < 1000:
            return True

    class Meta:
        verbose_name = "Publication"
        verbose_name_plural = "Publications"
        ordering = ['title', 'price']
        # order_with_respect_to = "rubric"

    def __str__(self):
        return self.title


class Spare(models.Model):
    name = models.CharField(max_length=20)


class Car(models.Model):
    name = models.CharField(max_length=20)
    spares = models.ManyToManyField(Spare, null=True)  # massive
