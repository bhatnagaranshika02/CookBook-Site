from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__ (self):
        return self.name

class Ingredients(models.Model):
    name = models.CharField(max_length=255)
    notes = TextField(max_length=255)

    category = models.ForeignKey(Category, related_names="ingredients", on_delete=models.CASCADE)

    def __str__ (self):
        return self.name


