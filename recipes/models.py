from django.db import models
from django.utils.text import slugify

from categories.models import Category
from users.models import Profile

class Recipe(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey( Category, on_delete=models.CASCADE )
    author = models.ForeignKey( Profile, on_delete=models.CASCADE )
    image = models.ImageField( upload_to='recipes/', null=False, blank=False )
    preparation = models.TextField()
    ingredients = models.TextField()
    slug = models.SlugField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True) 

    def save(self, *args, **kwargs):
        self.slug = slugify( self.title )
        super(Recipe, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
