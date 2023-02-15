from django.db import models

# Create your models here.
class Tag(models.Model):
  value = models.CharField(max_length=50)

  def __str__(self):
    return self.value

class Post(models.Model):
  title = models.CharField(max_length=125)
  content = models.TextField()
  summary = models.TextField(max_length=255)
  slug = models.SlugField(max_length=50)
  tags = models.ManyToManyField(Tag, blank=True)
  create_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now_add=True)
  published = models.DateTimeField(auto_now_add=False)
