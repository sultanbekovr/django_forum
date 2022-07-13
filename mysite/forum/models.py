from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)

class SubCategory(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

class Post(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    postImg = models.ImageField(upload_to='photos/post/%Y/%m/%d', blank=True)
    cat = models.ForeignKey('Category', on_delete=models.CASCADE)
    SubCat = models.ForeignKey('SubCategory', on_delete=models.CASCADE)
    views = models.IntegerField()
    ans = models.IntegerField()

class Ansewr(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    ansImg = models.ImageField(upload_to='photos/ans/%Y/%m/%d', blank=True)

class News(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    newsImg = models.ImageField(upload_to='photos/news/%Y/%m/%d')
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    cat = models.ForeignKey('Category', on_delete=models.CASCADE)

