from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db.models.signals import post_save


class User(AbstractUser):
    
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    UserName = models.CharField(max_length=100)
    Email = models.EmailField(unique=True)
    phone_number = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^\+?251?\d{9,15}$',
                message="Phone number must be entered in the format: '+251999999999'. Up to 15 digits allowed."
            ),
        ]
    )
    USERNAME_FIELD = 'Email'
    REQUIRED_FIELDS = ['UserName']
    
    def profile(self):
        profile = Profile.objects.get(user=self)
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=300)
    image = models.ImageField(upload_image='user_image')    
    
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objecte.create(user=instance)
    def save_user_profile(sender, created, **kwargs):
        instance.profile.save()
    post_save.connect(create_user_profile, sender=User)
    post_save.connect(save_user_profile, sender=User)        