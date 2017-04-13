from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel
from wagtail.wagtailadmin.edit_handlers import InlinePanel

from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey

@register_snippet
class Teacher(ClusterableModel):
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
      InlinePanel('courses', label="Courses"),
    ]
    def __str__(self):              # __unicode__ on Python 2
        return self.name


@register_snippet
class course(models.Model):
    teacher = ParentalKey('Teacher', related_name='courses')
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    date = models.DateField()
    time = models.TimeField(null=True, blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('location'),
        FieldPanel('date'),
        SnippetChooserPanel('teacher'),
    ]
    def __str__(self):              # __unicode__ on Python 2
        return "{} by {} - {} - {} {}".format(self.name,self.teacher,self.location,self.time,self.date)

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
    
