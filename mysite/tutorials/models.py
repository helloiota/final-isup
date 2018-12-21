from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.search import index

# Create your models here.
class TutorialsIndexPage(Page):
	intro = RichTextField(blank=True)

	def get_context(self, request):
		# Update context to include only published posts, ordered by reverse-chron
		context = super().get_context(request)
		tutorialpages = self.get_children().live().order_by('-first_published_at')
		context['tutorialpages'] = tutorialpages
		return context

	# content_panels = Page.content_panels + [
	# 	FieldPanel('intro', classname="full")
	# ]

class TutorialPage(Page):
	date = models.DateField("Post date")
	intro = models.CharField(max_length=250)
	body = RichTextField(blank=True)

	search_fields = Page.search_fields + [
		index.SearchField('intro'),
		index.SearchField('body'),
	]

	content_panels = Page.content_panels + [
		FieldPanel('date'),
		FieldPanel('intro'),
		FieldPanel('body', classname="full"),
	]
