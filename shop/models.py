from django.db import models
from pytz import timezone
from django.conf import settings
from django.urls import reverse

def local_time(input_time):
    fmt = '%Y-%m-%d %H:%M'
    my_zone = timezone(settings.TIME_ZONE)
    my_local_time = input_time.astimezone(my_zone)
    return my_local_time.strftime(fmt)

class Item(models.Model):
    name = models.CharField(max_length=20)
    desc = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField()
    tags = models.ManyToManyField('Tag', blank=True, related_name='tags')

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name

    def tagged(self):
        ts = self.tags.all()
        return  '{' + ', '.join(map(str, ts)) + '}'

        return tag_string
    tagged.short_description = '태그 집합'

    def updated(self):
        return local_time(self.updated_at)
    updated.short_description = '수정 일시'

    def get_absolute_url(self):
        return reverse('shop:item_detail', kwargs={'pk': self.pk})


class Review(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE,
                             related_name='reviews', verbose_name='아이템')
    message = models.TextField('상품후기')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-item__id', '-id']
    def updated(self):
        return local_time(self.updated_at)

    updated.short_description = '수정 일시'

    def __str__(self):
        return self.message



class Tag(models.Model):
    name = models.CharField('태그', max_length=100, unique=True)

    class Meta:
        ordering = ['-id']  # Tag 객체의 기본 정렬 순서 지정

    def __str__(self):
        return self.name

