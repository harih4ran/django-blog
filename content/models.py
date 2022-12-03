from django.db import models
import random
import string
from django.contrib.auth.models import User

def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))

class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.CharField(max_length=146)
    content = models.TextField(blank = True)
    created_on = models.DateTimeField(auto_now=True)
    thumbnail = models.ImageField(upload_to="thumbnail")
    status = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    @property    
    def total_comment(self):
        instance = Comment.objects.all().count()
        return str(instance)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug() + "-" + self.title)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name="comment_post",blank = True)
    name = models.CharField(max_length=150)
    email = models.EmailField(null = True,blank = True)
    body = models.TextField(null = True,blank = True)
    likes = models.ManyToManyField(User,related_name="comment_likes",blank = True)
    date_created = models.DateTimeField(auto_now_add=True)

    @property    
    def total_likes(self):
        instance = self.likes.all().count()
        return str(instance)

    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return self.body

class Newsletter(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(null = True,blank = True)
    to = models.EmailField(null = True,blank = True)
    comment = models.TextField(null = True,blank = True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return self.comment