from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager

from django.contrib.contenttypes.fields import GenericRelation

from hitcount.models import HitCountMixin
from hitcount.settings import MODEL_HITCOUNT


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Kategori')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='URL')
    description = models.TextField(verbose_name='Açıklama')

    class Meta:
        verbose_name = "Kategori"
        verbose_name_plural = "Kategoriler"

    def get_absolute_url(self):
        return reverse('list_by_category', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


class Article(models.Model, HitCountMixin):
    title = models.CharField(max_length=100, unique=True, verbose_name='Başlık')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL')
    description = models.CharField(max_length=255, verbose_name='Özet')
    content = RichTextField(blank=True, null=True, verbose_name='İçerik')
    image = models.ImageField(upload_to="upload/article/images/%Y/%m/%d/", verbose_name='Resim')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Kategori')
    tags = TaggableManager(verbose_name='Etiket')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Yazar')
    status = models.BooleanField(default=False, verbose_name='Yayında')
    featured = models.BooleanField(default=False, verbose_name='Manşet')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Tarih')
    updated = models.DateTimeField(auto_now=True, verbose_name='Güncelleme')
    hit_count_generic = GenericRelation(
        MODEL_HITCOUNT, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation')

    class Meta:
        ordering = ['-created']
        verbose_name = "Haber"
        verbose_name_plural = "Haberler"

    def get_absolute_url(self):
        return reverse('article_detail',
                       kwargs={'slug': self.slug, 'pk': self.pk})  # haber/id/slug şeklinde olması için

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, related_name="comments", verbose_name="Haber", on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name="Ad")
    email = models.EmailField(max_length=100, verbose_name="E-Mail")
    body = models.TextField(max_length=1000, verbose_name="Yorum")
    active = models.BooleanField(default=False, verbose_name="Yayında")
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']
        verbose_name = "Yorum"
        verbose_name_plural = "Yorum"

    def __str__(self):
        return self.name
