from datetime import date
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from dateutil.relativedelta import relativedelta

# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='bee.png', upload_to='profile_images')
    bio = models.TextField()
    phone = models.CharField(max_length=13, default='+91')
    dob = models.DateField(default=date.today,max_length=8)
    def __str__(self):
        today = date.today()
        delta = relativedelta(today, self.dob)
        return str(delta.years)
    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 150 or img.width > 150:
            new_img = (150, 150)
            img.thumbnail(new_img)
            img.save(self.avatar.path)
