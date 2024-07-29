from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name

def get_default_author():

    author, created = Author.objects.get_or_create(name='Default Author')
    return author.id

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,default=get_default_author)

    def __str__(self):
        return self.title
