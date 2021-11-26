from django.contrib.auth.models import User
from django.db import models
# from django.db.models.signals import post_save
# from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(default="upload/profile/photo/default.jpg", upload_to="upload/profile/photo/", verbose_name='Fotoğraf')
    bio = models.CharField(max_length=255, verbose_name='Biyografi')
    web = models.URLField(verbose_name='Web')
    facebook = models.URLField(verbose_name='Facebook')
    youtube = models.URLField(verbose_name='Youtube')
    twitter = models.URLField(verbose_name='Twitter')
    instagram = models.URLField(verbose_name='Instagram')

    class Meta:
        verbose_name = "Profil"
        verbose_name_plural = "Profil"

    def __str__(self):
        return self.user.username


# @receiver(post_save, sender=User)
# def create_or_update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()
