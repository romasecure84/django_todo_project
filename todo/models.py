from django.db import models
from autoslug import AutoSlugField

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True,)

    def __str__(self):
        return self.title

class Todo(models.Model):
    #category = models.ForeignKey(Category, on_delete=models.CASCADE) # Bu usulla kateqoriya silinende, elaqeli hamisi silinir
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=False)
    cerated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title