from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User


class Box(models.Model):
    
    label = models.CharField(_("label"), max_length=100, db_index=True)
    content = models.TextField(_("content"))
    language = models.CharField(_("language"),
        max_length = 10,
        choices = getattr(settings, "LANGUAGES", []),
        default = getattr(settings, "LANGUAGE_CODE", None),
        null = True,
        blank = True
    )
    
    created_by = models.ForeignKey(User, related_name="boxes")
    last_updated_by = models.ForeignKey(User, related_name="updated_boxes")
    
    def __unicode__(self):
        return self.label
    
    class Meta:
        verbose_name_plural = "boxes"
        unique_together = ["label", "language"]
