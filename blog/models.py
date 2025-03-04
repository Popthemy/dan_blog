from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


# Create your models here.
class Story(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200,unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-updated_at',)
        verbose_name = _('Story',)
        verbose_name_plural = _('Stories',)
        indexes = (
            models.Index(fields=('updated_at',)),
        )

    def __str__(self):
        return f'{self.title} by {self.author}'

    def get_absolute_url(self):
        '''get the url to the story detail'''
        return reverse("story_detail", kwargs={"pk": self.pk})
