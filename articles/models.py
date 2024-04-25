from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils import timezone
from django.urls import reverse

from .utils import slugify_instance_title
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now, null=True, blank=True)

    def get_absolute_url(self):
        return reverse("article-detail", kwargs={"slug": self.slug})



def article_pre_save_receiver(sender, instance, *args, **kwargs):
    if instance.slug is None:
        slugify_instance_title(instance, save=False)

pre_save.connect(article_pre_save_receiver, sender=Article)

def article_post_save_receiver(sender, instance, created, *args, **kwargs):
    if created:
        slugify_instance_title(instance, save=True)

post_save.connect(article_post_save_receiver, sender=Article)