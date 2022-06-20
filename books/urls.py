from django.urls import path
from books import views

urlpatterns = [
    path('titles', views.TitleListAPIView.as_view()),
    path('titles/<title_id>', views.TitleRetrieveAPIView.as_view()),
    path('titles/<title_id>/volume/<volume_id>', views.VolumeRetrieveAPIView.as_view()),
    path('titles/<title_id>/volume/<volume_id>/chapter/<chapter_id>', views.ChapterRetrieveAPIView.as_view()),
]
