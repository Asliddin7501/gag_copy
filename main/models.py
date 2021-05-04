from django.db import models
from gag.helpers import UploadTo
from gag.mixins import TranslateMixin
from django.utils.translation import gettext_lazy as _


class Category(TranslateMixin, models.Model):
    translate_fields = ['name']

    name_uz = models.CharField(max_length=50)
    name_ru = models.CharField(max_length=50)
    image = models.ImageField(max_length=100, upload_to=UploadTo("category"))
    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"
    def __str__(self):
        return self.name


class Post(models.Model):
    user = models.ForeignKey("client.User", on_delete=models.RESTRICT)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, verbose_name=_("Kategoriya"))
    comment = models.TextField(verbose_name=_("Izoh"))
    file = models.FileField(max_length=100, verbose_name=_("Rasm/Video"), upload_to=UploadTo("post"))
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PostComment(models.Model):
    parent = models.ForeignKey('PostComment', on_delete=models.RESTRICT, null=True, default=None)
    post = models.ForeignKey('main.Post', on_delete=models.RESTRICT)
    user = models.ForeignKey('client.User', on_delete=models.RESTRICT)
    comment = models.TextField(default=None, null=True)
    image = models.ImageField(max_length=100, upload_to=UploadTo("comment"))
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)