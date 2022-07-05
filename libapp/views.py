from django.http import JsonResponse
from django.core.handlers.wsgi import WSGIRequest

from .models import Book


def find_author_by_id(request:WSGIRequest, author_id: int) -> JsonResponse:
    """Поиск автора и его книг в 1 запрос к БД"""

    book_list = Book.objects.filter(author_id=author_id)
    if len(book_list):
        to_ret_dict = book_list[0].author.as_json()
        to_ret_dict['books'] = [item.as_json() for item in book_list]
        return JsonResponse(to_ret_dict)

    else: return JsonResponse({"id": 0, "name": "", "books": []})