from django.db import models

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=300)

class Diet(models.Model):
    diet = models.CharField(max_length=300)

class MenuItems(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=1000)
    price = models.FloatField()
    spice = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    diet = models.ForeignKey(Diet, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + " " + self.description + "  $" + str(self.price)
  
