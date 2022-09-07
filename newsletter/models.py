from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class EmailSub(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='First Name')
    last_name = models.CharField(max_length=50, verbose_name='Last Name')
    em_address = models.EmailField(verbose_name='Email')

    def __str__(self):
        return self.first_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Email(models.Model):
    subject = models.CharField(max_length=30, verbose_name='Subject')
    content = RichTextField()
