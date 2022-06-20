from django.db import models
from django.utils.translation import gettext as _


class Title(models.Model):
    ru_name = models.CharField(_('ru_name'), max_length=120)
    en_name = models.CharField(_('en_name'), max_length=120)
    alter_name = models.CharField(_('alter_name'), max_length=120)
    description = models.TextField(_('description'))

    def __str__(self):
        return f'{self.en_name}'

    class Meta:
        verbose_name = _('Title')
        verbose_name_plural = _('Titles')


class Volume(models.Model):
    title = models.ForeignKey(
        Title,
        models.CASCADE,
        related_name='volumes',
        verbose_name=_('Title')
    )
    name = models.CharField(_('name'), max_length=120)
    price = models.IntegerField(_('price'))
    volume_number = models.IntegerField(_('volume_number'))

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _('Volume')
        verbose_name_plural = _('Volumes')
        constraints = [
            models.UniqueConstraint(fields=['title', 'volume_number'], name='unique volume_number')
        ]


class Chapter(models.Model):
    volume = models.ForeignKey(
        Volume,
        models.CASCADE,
        related_name='chapters',
        verbose_name=_('Volume')
    )
    chapter_number = models.IntegerField(_('chapter_number'))
    content = models.TextField(_('content'))
    likes = models.IntegerField(_('likes'), default=0)
    views = models.IntegerField(_('views'), default=0)

    def __str__(self):
        return f'{self.chapter_number}'

    class Meta:
        verbose_name = _('Chapter')
        verbose_name_plural = _('Chapters')
        constraints = [
            models.UniqueConstraint(fields=['volume', 'chapter_number'], name='unique chapter_number')
        ]


class Tag(models.Model):
    name = models.CharField(max_length=100)
    titles = models.ManyToManyField(Title, 'tags')
