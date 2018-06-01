from __future__ import unicode_literals
from django.conf import settings

from django.db import models
from django.contrib.postgres.fields import ArrayField

from django.utils.encoding import smart_text as smart_unicode
from django.utils.translation import ugettext_lazy as _


class Media(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    filename = models.CharField(_("Filename"), max_length=255)
    mediatype = models.CharField(_("Media Type"), max_length=255)
    path = models.CharField(_("Path"), max_length=255)
    uri = models.CharField(_("uri"), max_length=255)
    tags = ArrayField(ArrayField(models.CharField(max_length = 5000)))
    date_created = models.DateTimeField(_("Date Created"), auto_now_add=True)

    class Meta:
        verbose_name = _("Media")
        verbose_name_plural = _("Media")

    def __unicode__(self):
        return smart_unicode(self.name)
