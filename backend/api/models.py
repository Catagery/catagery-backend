from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name



class Purchase(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    price = models.FloatField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name