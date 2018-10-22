# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.contrib import admin
from blog import views
from django.views.generic import FormView

urlpatterns = [
	url('^$', views.index, name='posts'),
	url('index/$', views.PostListView.as_view(), name='posts'),
	url(r'^(?P<pk>\d+)/$', views.PostDetailView.as_view(), name='post-view'),
	url(r'^(?P<slug>[-\w\d]+)/$', views.PostDetailView.as_view(), name='post-view'),

	#url('^index/', views.index, name='posts'),
	#url('^$', views.PostListView.as_view(), name='posts'),
	#url(r'^/(?P<pk>\d+)/$', views.PostDetailView.as_view(), name='post-view'),
	#url(r'^/(?P<slug>[-\w\d]+)/$', views.PostDetailView.as_view(), name='post-view'),
]
