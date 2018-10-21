# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic
from blog.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):

	posts_list = Post.objects.filter(publish = True)
	page = request.GET.get('page', 1)
	paginator = Paginator(posts_list, 5)

	try:
		selected_page = paginator.page(page)
	except PageNotAnInteger:
		selected_page = paginator.page(1)
	except EmptyPage:
		selected_page = paginator.page(paginator.num_pages)

	context = {
		'posts' : selected_page,
	}

	# Render the HTML template index.html with the data in the context variable
	return render(request, 'posts.html', context=context)

class PostListView(generic.ListView):
    model = Post

class PostDetailView(generic.DetailView):
	model = Post

def projects(request):

	project_list = Project.objects.filter(publish = True)
	post_list = Post.objects.filter(publish = True)

	for project in project_list:
		project.associated_posts = []
		for post in post_list:
			if project.project_id in [x.__str__() for x in post.tags.all()]:
				project.associated_posts.append(post)

	context = {
		'projects' : project_list
	}

	return render(request, 'projects.html', context = context)

def about(request):

    bio = Biography.objects.filter(publish=True)

    context = {
		'bio' : bio,
	}

    return render(request, 'aboutme.html', context = context)
	#return render(request, 'about.html', {})

# Replaced dedicated page with contact buttons in nav bar
#def contact(request):
#	return render(request, 'contact.html', {})

def resume(request):
	return render(request, 'alexandersiemanresume.pdf', {})



