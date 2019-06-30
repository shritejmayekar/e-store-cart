from django.db import models
from products.models import Product
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    email = models.EmailField()
    address = models.CharField(max_length=160)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return 'Order {}'.format(self.id)

    # def get_total_cost(self):
    #     return sum(item.get_cost() for item in self.items.all())
class OrderItem(models.Model):
    order = models.ForeignKey(Order,related_name='orders',on_delete = models.CASCADE)
    product = models.ForeignKey(Product,related_name='products',on_delete = models.CASCADE)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
   