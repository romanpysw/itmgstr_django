from django.urls import path

from . import views

urlpatterns = [
    path('writers/<int:author_id>', views.find_author_by_id),
]