from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailsnippets.models import register_snippet

@register_snippet
class Teacher(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    website = models.CharField(max_length=250)
    photo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    bio = RichTextField(blank=True)
    
    panels = [
      FieldPanel('name'),
      FieldPanel('phone'),
      FieldPanel('email'),
      FieldPanel('website'),
      FieldPanel('bio', classname="full"),
      ImageChooserPanel('photo'),
    ]
    def __str__(self):              # __unicode__ on Python 2
        return self.name

class HomePage(Page):
    body = RichTextField(blank=True)
    photo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    
    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        ImageChooserPanel('photo')
    ]
    
class StandardPage(Page):
    link_name = models.CharField(max_length=50)
    body = RichTextField(blank=False)
    
    content_panels = Page.content_panels + [
        FieldPanel('link_name'),
        FieldPanel('body', classname="full"),
    ]