from django.db import models
from django.utils import timezone

# Create your models here.

# https://stackoverflow.com/questions/39398031/django-booleanfield-as-a-dropdown


class Post(models.Model):
    name_choices = ((True, 'boast'), (False, 'roast'))
    content = models.CharField(max_length=100)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    submission_time = models.DateTimeField(default=timezone.now)
    name_post = models.BooleanField(choices=name_choices)

    def __str__(self):
      return f"{self.content}"
