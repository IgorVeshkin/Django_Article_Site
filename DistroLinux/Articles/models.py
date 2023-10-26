from django.conf import settings
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=False)
    author = models.CharField(max_length=100)
    theme = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to="static/images/uploaded/%Y/%m/%d/")
    creation_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        if not self.theme:
            self.theme = "Linux"
        return reverse('show-article', kwargs={"theme": self.theme, "article_pk": self.pk})
        # return reverse('article', kwargs={"theme": self.theme})

    class Meta:
        ordering = ['-creation_time', ]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    profile_image = models.FileField(blank=True, upload_to="static/images/users/profile-images/")
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.user.username, self.user.email)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

