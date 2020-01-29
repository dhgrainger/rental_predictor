from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Post(models.Model):
 title = models.CharField(max_length=100)
 slug  = models.SlugField()
 text  = models.TextField()
 pub_date = models.DateField('date_published', auto_now_add=True)
 city = models.ForeignKey('City', on_delete=models.CASCADE)

def __str__(self):
  return "{} on {}".format(
   self.title,
   self.pub_date.strftime('%Y-%m-%m'))

class Meta:
  verbose_name = 'investment thesis'
  ordering = ['-pub_date', 'title']
  get_latest_by = 'pub_date'

class City(models.Model):
 name = models.CharField(max_length=100)
 slug = models.SlugField()
 description = models.TextField()
 pe_ratio = models.DecimalField(max_digits=7, decimal_places=2)

def __str__(self):
  return self.name

class Meta:
  ordering = ['name']
