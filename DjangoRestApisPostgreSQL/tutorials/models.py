from django.db import models


class Income(models.Model):
    amount = models.DecimalField(
        max_digits=10, decimal_places=2
    )  # Сумма до 99999999.99
    description = models.CharField(max_length=255)  # Описание до 255 символов
    date = models.DateField()  # Дата дохода
    created_at = models.DateTimeField(auto_now_add=True)  # Время создания записи

    def __str__(self):
        return f"{self.amount} - {self.description}"


class Category(models.Model):
    name = models.CharField(
        max_length=100
    )  # Название категории (например, "Еда", "Транспорт")

    def __str__(self):
        return self.name


class Expense(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Сумма
    description = models.CharField(max_length=255)  # Описание
    date = models.DateField()  # Дата расхода
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )  # Категория (может быть null)
    created_at = models.DateTimeField(auto_now_add=True)  # Время создания

    def __str__(self):
        return f"{self.amount} - {self.description}"
