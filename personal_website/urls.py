"""alexandersieman URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
from blog import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

# Map URLs to blog/urls.py
urlpatterns += [
	#url(r'^blog/', include('blog.urls')),
    url(r'^posts/', include('blog.urls')),
]

# Remap the base URL of the site to the blog
urlpatterns += [
	#url(r'^$', RedirectView.as_view(url = '/blog/')),
    url(r'^$', RedirectView.as_view(url = '/posts/')),
]

urlpatterns += [
    url(r'^projects/',views.projects, name='projects'),
    url(r'^about/',views.about, name='about'),
    #url(r'^contact/',views.contact, name='contact'),
    url(r'^resume/',views.resume, name='resume'),
]
