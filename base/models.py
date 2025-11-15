from django.db import models

from django_ckeditor_5.fields import CKEditor5Field


class BaseModel(models.Model):
    """A simple reusable base model for all apps."""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True 
        ordering = ['id']

    def __str__(self):
        return f"{self.__class__.__name__} (id={self.pk})"

class Banner(BaseModel):
    file = models.FileField(upload_to="banner")
    text = models.CharField(max_length=500)


class Gellery(BaseModel):
    image = models.FileField(upload_to="gellery")


class Info(BaseModel):
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    logo = models.FileField(upload_to='logo')

    about_school = CKEditor5Field()
    school_image = models.FileField()
    school_image_sec = models.FileField()



class Porichalok(BaseModel):
    name = models.CharField(max_length=500)
    text = CKEditor5Field()
    title = models.CharField(max_length=500)
    image = models.FileField(upload_to="teachers")

class HeadTeacher(BaseModel):
    name = models.CharField(max_length=500)
    text = CKEditor5Field()
    title = models.CharField(max_length=500)
    image = models.FileField(upload_to="teachers")


class Category(BaseModel):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Notice(BaseModel):
    title = models.CharField(max_length=200)
    text = CKEditor5Field()

class Subcategory(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategories")
    name = models.CharField(max_length=50)
    text = CKEditor5Field()

class Widget(BaseModel):
    title = models.CharField()
    image = models.FileField(upload_to='teachers')
    text = CKEditor5Field()

class MaddhomikTeacher(BaseModel):
    title = models.CharField()
    image = models.FileField(upload_to='teachers')
    text = CKEditor5Field()


