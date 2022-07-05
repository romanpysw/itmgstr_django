from django.core.management.base import BaseCommand
from django.core.management import call_command
from ...models import Writer, Book


def create_authors_rows() -> None:
    """Внесение строк авторов в БД"""

    Writer.objects.create(name='A. Pushkin')
    Writer.objects.create(name='M. Lermontov')
    Writer.objects.create(name='L. Tolstoi')
    Writer.objects.create(name='A. Blok')

def create_books_rows() -> None:
    """Внесение строк книг в БД"""

    Book.objects.create(name='Capitans daughter', author=Writer.objects.get(name='A. Pushkin'))
    Book.objects.create(name='Tale adout king Saltan', author=Writer.objects.get(name='A. Pushkin'))
    Book.objects.create(name='Mtsyri', author=Writer.objects.get(name='M. Lermontov'))
    Book.objects.create(name='Hello World by Lermontov', author=Writer.objects.get(name='M. Lermontov'))
    Book.objects.create(name='War and Peace', author=Writer.objects.get(name='L. Tolstoi'))
    Book.objects.create(name='Hello world by Tolstoi', author=Writer.objects.get(name='L. Tolstoi'))
    Book.objects.create(name='Trinadtsat', author=Writer.objects.get(name='A. Blok'))



class Command(BaseCommand):
    help = 'Создание таблиц в базе данных и заполнение их тестовыми данными'

    def handle(self, *args, **kwargs):
        """Обработчик функции"""

        # Вызов миграции
        call_command('migrate', 'libapp')

        # Внесение строк авторов
        create_authors_rows()

        # Внесение строк книг
        create_books_rows()
        