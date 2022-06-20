from rest_framework import serializers

from books.models import Title, Volume, Chapter


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = '__all__'


class VolumeSerializer(serializers.ModelSerializer):
    chapters = ChapterSerializer(many=True)

    class Meta:
        model = Volume
        fields = '__all__'


class TitleSerializer(serializers.ModelSerializer):
    volumes = VolumeSerializer(many=True)

    class Meta:
        model = Title
        fields = '__all__'
