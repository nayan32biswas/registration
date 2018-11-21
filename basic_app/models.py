from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfileInfoModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    protfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __self__(self):
        return self.user.username
