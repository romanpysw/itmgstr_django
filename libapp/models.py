from django.db import models

# Create your models here.

class Writer(models.Model):
    """Класс Писателя"""

    # Имя писателя
    name = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name

    def as_json(self) -> dict:
        """Представление объекта в JSON-сериализуемом виде"""
        return {'id': self.id, 'name': self.name}


class Book(models.Model):
    """Класс Книги"""

    # Название книги
    name = models.CharField(max_length=400)

    # Внешний ключ на писателя, где у 1 писателя может быть несколько книг
    author = models.ForeignKey(Writer, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

    def as_json(self) -> dict:
        """Представление объекта в JSON-сериализуемом виде"""
        return {'id': self.id, 'name': self.name}