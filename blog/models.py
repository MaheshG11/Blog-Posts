from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse



class Post(models.Model) : #inherted form Model
    title  = models.CharField(max_length=100) 
    content = models.TextField() 
    date_posted=models.DateTimeField(default=timezone.now)#auto_now=True(everytime a post is updated it date_posted gets updated)
                                                    #auto_now_add=True(when post is create the date_posted gets added)
                                                    #we do not want the actual function to be executed so we did not used () 
                                                    # we only passed the function for timezone.now 
    Author=models.ForeignKey(User,on_delete=models.CASCADE)

# Create your models here.
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})