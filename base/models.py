from django.db import models

from django_ckeditor_5.fields import CKEditor5Field


class BaseModel(models.Model):
    """A simple reusable base model for all apps."""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True 
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.__class__.__name__} (id={self.pk})"

class Banner(BaseModel):
    file = models.FileField(upload_to="banner")
    text = models.CharField(max_length=500)

class Info(BaseModel):
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    email = models.CharField(max_length=500)


class Porichalok(BaseModel):
    name = models.CharField(max_length=500)
    text = CKEditor5Field()
    title = models.CharField(max_length=500)
    image = models.FileField(upload_to="teachers")

