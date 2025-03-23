from django.db import models

# Create your models here.

class StoryData(models.Model):
    by = models.CharField(max_length=20) # author
    descendants = models.IntegerField() # num of comments
    post_id = models.CharField(max_length=15) # story id
    score = models.IntegerField() # num of views
    time = models.DateTimeField() # time
    title = models.CharField(max_length=300) # story title
    type = models.CharField(max_length=15) # type(job, story, ...)
    url = models.URLField() # link
    content = models.TextField(max_length=100000) # story content

    def __str__(self):
        return self.title

class Post(models.Model):
    postname = models.CharField(max_length=50)
    contents = models.TextField()

    def __str__(self):
        return self.postname
