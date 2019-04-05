from django.db import models
from PIL import Image
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default = 'default.jpg',upload_to='profile_pics',blank=False)

    def __str__(self):
        return f"{self.user.username} profile"


    # def save():
    #     super().save()
    #     img = Image.open(self.avatar.path)
    #     if img.height > 128:
    #         div = img.height/128
    #         out_size = (int(img.width/div),128)
    #     elif img.width > 128:
    #         div = img.width/128
    #         out_size = (128,int(img.height/div))
    #     else:
    #         out_size =(img.width,img.height)
    #     img.thumbnail(out_size)
    #     img.save(self.avatar.path)

def create_avatar(sender, **kwargs):
    if kwargs['created']:
        user_profile= Profile.objects.create(user=kwargs['instance'])
post_save.connect(create_avatar, sender=User)
