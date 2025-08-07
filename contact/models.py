from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(upload_to='contact_pictures/%Y/%m/%d/', blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='contacts', blank=True, null=True)
    birthday = models.DateField(verbose_name='Data de Nascimento', blank=True, null=True)
    
    

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'