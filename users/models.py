from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)#cascade means that if the user is deleted then the profile will be deleted 
                                                            #but if the profile is deleted then user won't be deleted 

    img=models.ImageField(default='default.jpeg',upload_to='profile_pics')
    def __str__(self) :
        return f'{self.user.username} Profile'
    

    def save(self):#NOW we will use this function to save our image 

        super().save()
        IMG=Image.open(self.img.path)
        if(IMG.height>300 or IMG.width>300):
            IMG.thumbnail((300,300))
            IMG.save(self.img.path)