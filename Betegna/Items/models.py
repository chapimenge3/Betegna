from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe

# project import 
from .utils import item_directory_path


class Category(models.Model):
    category = models.CharField(_("Category"), max_length=50)

    def __str__(self) -> str:
        return self.category


class Item(models.Model):
    name = models.CharField(_("Name"), max_length=150)
    price = models.DecimalField(_("Price"), max_digits=10, decimal_places=2)
    description = models.CharField(
        _("Description"), max_length=200, blank=True, default="")
    stars = models.IntegerField(_("Stars"))
    image = models.ImageField(
        _("Image"),
        upload_to=item_directory_path,
    )
    
    def __str__(self) -> str:
        return self.name
    
    def image_tag(self):
        return mark_safe('<img src="%s" width="150" height="150"/>' % self.image.url)

    image_tag.short_description = 'Photo'
    image_tag.allow_tags = True

