from rest_framework.generics import ListAPIView, RetrieveAPIView

from books.models import Title, Chapter, Volume
from books.serializers import TitleSerializer, VolumeSerializer, ChapterSerializer
from books.tasks import increment_chapter_views


class TitleListAPIView(ListAPIView):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer


class TitleRetrieveAPIView(RetrieveAPIView):
    serializer_class = TitleSerializer

    def get_object(self):
        return Title.objects.get(pk=self.kwargs['title_id'])


class VolumeRetrieveAPIView(ListAPIView):
    serializer_class = VolumeSerializer

    def get_object(self):
        return Volume.objects.get(
            title_id=self.request.kwargs['title_id'],
            pk=self.request.kwargs['volume_id']
        )


class ChapterRetrieveAPIView(ListAPIView):
    serializer_class = ChapterSerializer

    def get_object(self):
        increment_chapter_views.delay(self.request.kwargs['chapter_id'])
        return Volume.objects.get(
            volume__title_id=self.request.kwargs['title_id'],
            volume_id=self.request.kwargs['volume_id'],
            pk=self.request.kwargs['chapter_id']
        )
