from celery import shared_task
from django.db.models import F

from books.models import Chapter


@shared_task
def increment_chapter_like(chapter_pk):
    Chapter.objects.filter(pk=chapter_pk).update(likes=F('likes') + 1)


@shared_task
def increment_chapter_views(chapter_pk):
    Chapter.objects.filter(pk=chapter_pk).update(views=F('views') + 1)
