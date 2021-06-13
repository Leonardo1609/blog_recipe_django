from django.db import models

from django.contrib.auth.models import User
from django.utils.text import slugify

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    url = models.CharField(max_length=200)
    image = models.ImageField(upload_to='users/')
    slug = models.SlugField(null=False, unique=False, blank=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username

