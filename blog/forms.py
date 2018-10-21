
from django import forms
from pagedown.widgets import AdminPagedownWidget
from .models import Post, Project, Biography

class PostForm(forms.ModelForm):

	content = forms.CharField(widget=AdminPagedownWidget())

	class Meta:
		model = Post
		fields = [
			"title",
			"author",
			"tags",
			"content",
			"slug",
			"publish",
		]

class ProjectForm(forms.ModelForm):

	project_overview = forms.CharField(widget=AdminPagedownWidget())

	class Meta:
		model = Project
		fields = [
			"title",
			"project_id",
			"project_overview",
			"publish",
		]

class BiographyForm(forms.ModelForm):

	content = forms.CharField(widget=AdminPagedownWidget())

	class Meta:
		model = Biography
		fields = [
			"title",
			"content",
			"publish",
		]
