# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from markdown_deux import markdown
from django.utils.safestring import mark_safe


class Tag(models.Model):

	slug = models.SlugField(max_length = 200, unique = True)

	def __str__(self):
		return self.slug

	class Meta:
		verbose_name = 'Tag'
		verbose_name_plural = 'Tags'

class Post(models.Model):

	title = models.CharField(max_length = 250, unique = True)
	author = models.ForeignKey(User)
	tags = models.ManyToManyField(Tag)
	content = models.TextField()
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)

	slug = models.SlugField(max_length = 250, unique = True, default = '')
	publish = models.BooleanField(default = True, verbose_name = 'Publish to Web?')

	def get_absolute_url(self):
		return reverse('post-view', args=[str(self.slug)])

	def markdownize(self):
		return mark_safe(markdown(self.content))

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Post'
		verbose_name_plural = 'Posts'
		ordering = ['-created']

class Project(models.Model):

	title = models.CharField(max_length = 250, unique = True)
	project_id = models.SlugField(max_length = 250, unique = True, default = '')
	project_overview = models.TextField()
	created = models.DateTimeField(auto_now_add = True)
	publish = models.BooleanField(default = True, verbose_name = 'Publish to Web?')

	def get_absolute_url(self):
		return reverse('post-view', args=[str(self.project_id)])

	def markdownize(self):
		return mark_safe(markdown(self.project_overview))

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Project'
		verbose_name_plural = 'Projects'
		ordering = ['-created']

class SingletonModel(models.Model):

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.__class__.objects.exclude(id=self.id).delete()
        super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        try:
            return cls.objects.get()
        except cls.DoesNotExist:
            return cls()

# Will constitute the About page
class Biography(SingletonModel):

    title = models.CharField(max_length = 250, unique = True)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    publish = models.BooleanField(default = True, verbose_name = 'Publish to Web?')

    #def get_absolute_url(self):
    #    return reverse('post-view', args=[str(self.slug)])

    def markdownize(self):
        return mark_safe(markdown(self.content))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Biography'
        verbose_name_plural = 'Biographies'
        ordering = ['-updated']
