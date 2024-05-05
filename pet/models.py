from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True, null=True, unique=True)
    
    def __str__(self) -> str:
        return self.name
    
class Pet(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/pet")
    description = models.TextField()
    price = models.IntegerField()
    categories = models.ManyToManyField(Category, related_name='categories')
    added_by = models.ForeignKey(User, related_name="added_by", on_delete=models.CASCADE, blank=True, null=True)
    adopted_by = models.ForeignKey(User, related_name="adopted_by" , on_delete=models.CASCADE, blank=True, null=True)
    
    
    def __str__(self) -> str:
        return f'Pet name : {self.name}'