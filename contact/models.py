from django.db import models
from django.urls import reverse
from django.utils import timezone


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=2000)
    date_submitted = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "İletişim"
        verbose_name_plural = "İletişim"

    def get_absolute_url(self):
        return reverse('contact')

    def __str__(self):
        return self.name
