# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models
from forms import PostForm, ProjectForm, BiographyForm
from models import Post, Project, Biography

class PostAdmin(admin.ModelAdmin):
    form = PostForm
    fields = "__all__"

class EntryAdmin(admin.ModelAdmin):
	form = PostForm
	list_display = ('title', 'created')
	prepopulated_fields = {'slug' : ('title',)}

class ProjectAdmin(admin.ModelAdmin):
    form = ProjectForm
    list_display = ('title', 'created')

class BiographyAdmin(admin.ModelAdmin):
    form = BiographyForm
    list_display = ('title', 'created')

# Register your models here.
admin.site.register(models.Post, EntryAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.Biography, BiographyAdmin)
