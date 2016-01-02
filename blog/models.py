from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.core.urlresolvers import reverse

from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(_('title'), max_length=80)
    post = RichTextField(_('post'))
    tags = TaggableManager(blank=True)
    published = models.DateTimeField(_('published time'), auto_now_add=True)
    slug = models.SlugField(blank=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-published']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post', kwargs={'slug': self.slug})


class Subscriber(models.Model):
    email = models.EmailField(_('email'))

    class Meta:
        verbose_name = "Subscriber"
        verbose_name_plural = "Subscribers"

    def __str__(self):
        return self.email
