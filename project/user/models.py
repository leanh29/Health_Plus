from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class ProfileModel(models.Model):
    SEXUAL_CHOICES = (
        ('m', 'Male'),
        ('f', 'Female'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(default='profile_pics/default.png', upload_to='profile_pics')
    sexual = models.CharField(max_length=1, choices=SEXUAL_CHOICES, null=True)
    birthday = models.DateField(null=True)

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, force_insert=False,force_update=False, using=None, update_fields=None):
        super().save(force_insert,force_update, using, update_fields)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
