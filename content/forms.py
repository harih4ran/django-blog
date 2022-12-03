from django import forms
from content.models import *


class BlogForm(forms.ModelForm):
	class Meta:
		model = Blog
		fields = [
			"title",
			"description",
		]


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = [
			"context",
		]
