from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

class Post(models.Model):
	"""This class contains basic information about our model"""
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
	title = models.CharField(max_length = 200)
	text = models.TextField()
	date_created = models.DateTimeField(default = timezone.now())
	date_published = models.DateTimeField(null = True, blank = True)

	def __str__(self):
		return self.title