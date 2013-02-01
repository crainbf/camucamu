from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Author(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=40)

	def __unicode__(self):
		return u'%s %s' %(self.first_name, self.last_name)

class Book(models.Model):
	title = models.CharField(max_length=100)
	authors = models.ManyToManyField(Author)
	date_finished = models.DateField(blank=True, null=True)
	start_date = models.DateField(blank=True, null=True)
	pages = models.IntegerField(blank=True, null=True)
	subject_area= models.CharField(max_length=40, blank=True)
	language = models.CharField(max_length=40, blank=True)

	user = models.ForeignKey(User, blank=True, null=True)

	def get_authors(self):
		return "\n".join([a.last_name for a in self.authors.all()])

	def __unicode__(self):
		return self.title


