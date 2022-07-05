import uuid
import cloudinary
from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
from django.dispatch import receiver
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_controller = models.BooleanField(default=False)
    is_elder = models.BooleanField(default=False)
    is_resident = models.BooleanField(default=False)

    def __str__(self):
        return self.username


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Hood(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    about = models.TextField(max_length=255)
    slug = models.SlugField(null=False, unique=True)
    photo = cloudinary.models.CloudinaryField('image')

    def get_absolute_url(self):
        return reverse('hood_detail', kwargs={"slug": self.slug})

    def __str__(self):
        return self.name


class Service(models.Model):
    link = models.CharField(max_length=248)
    title = models.CharField(max_length=248)
    caption = models.TextField(max_length=2000)
    slug = models.SlugField(null=False, unique=True)
    photo = cloudinary.models.CloudinaryField('image')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE)
    created = models.DateTimeField('date created', default=timezone.now)

    def get_absolute_url(self):
        return reverse('service_detail', kwargs={"slug": self.slug})

    def __str__(self):
        return self.title


class Elder(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)
    photo = cloudinary.models.CloudinaryField('image')
    about = models.TextField()
    hood = models.ForeignKey(
        Hood, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.user.username


class Resident(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    email = models.CharField(max_length=100)
    photo = cloudinary.models.CloudinaryField('image')
    contact = models.CharField(max_length=10)
    about = models.TextField()
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Controller(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    email = models.CharField(max_length=100)
    photo = cloudinary.models.CloudinaryField('image')
    contact = models.CharField(max_length=10)
    about = models.TextField()
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username