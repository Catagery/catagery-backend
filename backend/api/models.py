from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    spended_sum = models.FloatField()
    
    def __str__(self):
        return self.name


class Category(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    title = models.CharField(null=True,max_length=200)
    color = models.CharField(null=True, max_length=20, blank=True)
    total_spend = models.FloatField(null=True, default=0)
    
    def __str__(self):
        return self.title
    
    @staticmethod
    def add_category():
        pass


class Purchase(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    date = models.DateField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.category.title

    @staticmethod
    def get_categoried_purchases(category, customer):
        p = Purchase.objects.filter(customer=customer)
        return p.filter(category__title=category)
    
    @staticmethod
    def get_all_purchases(customer):
        return Purchase.objects.filter(customer=customer)
    
    @staticmethod
    def get_purchases_by_date(customer, date):
        return Purchase.objects.filter(customer=customer).filter(date=date)
        
    
    @staticmethod
    def add_purchase():
        pass
    
    def delete(self, *args, **kwargs):
        self.category.total_spend -= self.price
        self.category.save()
        super(Purchase, self).delete(*args, **kwargs)

