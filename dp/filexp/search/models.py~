from django.db import models
from login.models import UserProfile
import datetime
class Page(models.Model):
     profile = models.ManyToManyField(UserProfile)
     title = models.CharField(max_length=100)
     url = models.URLField(max_length=200)
     datetime = models.DateTimeField('date_publish')
     def __str__(self):              
        return self.title
     
     

class Expression(models.Model):
      page = models.ForeignKey(Page)
      exp_text = models.CharField(max_length=50,blank=True)
      rating = models.IntegerField(default=0)
      def __str__(self):             
        return self.exp_text
