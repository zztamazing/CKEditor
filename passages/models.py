from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Passage(models.Model):
    content = RichTextUploadingField(verbose_name='正文部分', config_name='default')
