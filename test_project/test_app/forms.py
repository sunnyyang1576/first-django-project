
from django import forms
from .models import Blog, Author


class BlogForm(forms.ModelForm):

    author_name = forms.CharField(max_length=100, label='Author')

    class Meta:
        model = Blog
        fields = ['title', "author_name",'content']

    def save(self, commit=True):
        author_name = self.cleaned_data['author_name']
        author, created = Author.objects.get_or_create(name=author_name)
        self.instance.author = author
        return super().save(commit=commit)