from django.db import models


# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=17)
    address = models.CharField(max_length=400)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f'Client: {self.name}\n'
                f'Email: {self.email}\n'
                f'Registered: {self.registration_date}')


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=19)
    quantity = models.PositiveIntegerField()
    list_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return (f'Product: {self.name}\n'
                f'Price: {self.price}\n'
                f'{self.description}')


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    order_sum = models.DecimalField(decimal_places=2, max_digits=19, default=0)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f'{self.client.name}\n'
                f'{self.products}\n'
                f'{self.order_sum}')
