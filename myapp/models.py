from django.db import models

# Create your models here.
import datetime
from django.utils import timezone

class Post(models.Model):
	"""docstring for Post"""
	title = models.CharField(max_length = 32, unique = True);
	content = models.TextField(max_length = 200);
	likes = models.IntegerField();
	stars = models.DecimalField(max_digits = 10, decimal_places = 4);
	created = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.title