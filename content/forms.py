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
			"name",
			"email",
			"body",
		]

class NewsLetterForm(forms.ModelForm):
	class Meta:
		model = Newsletter
		fields = [
			"name",
			"email",
			"to",
			"comment",
		]