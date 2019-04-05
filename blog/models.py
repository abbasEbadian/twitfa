from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    last_modify_date = models.DateTimeField(auto_now=True)
    content = models.TextField(max_length=140,)
    likes = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        ending ={1:'st',2:'nd',3:'rd'}
        def get_end(m):
            if m in ending:
                return ending.get(m)
            else:
                return 'th'
        return f"{self.user.username}'s {self.id}{get_end(self.id)} Post."
