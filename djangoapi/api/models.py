from django.db import models
from django.contrib.auth.models import User

class NeedSimran(models.Model):
	title = models.CharField(max_length=100)
	desc = models.TextField()
	def __str__(self):
		return self.title

class NeedHelp(models.Model):
	title = models.CharField(max_length=100)
	desc = models.TextField()
	def __str__(self):
		return self.title

class NeedAdvice(models.Model):
	title = models.CharField(max_length=100)
	desc = models.TextField()
	def __str__(self):
		return self.title

class ProjectIdea(models.Model):
	title = models.CharField(max_length=100)
	desc = models.TextField()
	prob = models.TextField()
	def __str__(self):
		return self.title