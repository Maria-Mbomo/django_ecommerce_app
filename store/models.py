from django.db import models

# Create your models here.

class Promotion(models.Model):
    description =models.CharField(max_length=255) 
    discount = models.FloatField()
    #product_set
    
    
class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='+')
    #ie django will not create the reverse rlshp with prdt

class Product(models.Model):
    title =models.CharField(max_length=255)
    slug =  models.SlugField()
    description = models.TextField()
    #9999.99,for money values, decimalfields always better
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotion)
    
    #if we delete the collection, we dont delete the products with it...protect!
    #if the parent class cannot come before the child in the code,
    #you can simply pass the class into ''. ex: 'Collection', on_de... etc
    
    
    
class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'
    
    MEMBERSHIP_CHOICES =[
        (MEMBERSHIP_BRONZE,'Bronze'),
        (MEMBERSHIP_SILVER,'Silver'),
        (MEMBERSHIP_GOLD,'Gold')
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, 
                                  choices=MEMBERSHIP_CHOICES, 
                                  default=MEMBERSHIP_BRONZE)
    
    class Meta:
        db_table = 'store_customers'
        indexes = [
            models.Index(fields=['last_name', 'first_name'])
        ]
    
class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'
    
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed')
    ]
    placed_at = models.DateField(auto_now_add=True)#auto populates when we create an order
    payment_status = models.CharField(max_length=1,
                                      choices=PAYMENT_STATUS_CHOICES ) 
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    
    
    
class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # si on supprime le customer(parent), l'addresse disparait aussi,
    #d'ou le cascade
    #un client peut avoir many adresses, so one to many rlshp
  

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()


class OrderItem(models.Model):
    order=  models.ForeignKey(Order, on_delete=models.PROTECT)
    #si je supprime le parent(order), l'enfant part aussi(item)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6,decimal_places=2)
    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
      