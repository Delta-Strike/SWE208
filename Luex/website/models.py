from django.db import models
from shortuuid.django_fields import ShortUUIDField
# Create your models here.


class Category(models.Model):
    CID = ShortUUIDField(unique=True, length=10, max_length=25, prefix='catID')
    Name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='pics')

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.Name

# class Banner (models.Model):
#     Name=models.CharField(max_length=50)
#     Image=models.ImageField()


class Product(models.Model):
    Rating_Choices = (
        ('⭐✰✰✰✰', '1'),
        ('⭐⭐✰✰✰', '2'),
        ('⭐⭐⭐✰✰', '3'),
        ('⭐⭐⭐⭐✰', '4'),
        ('⭐⭐⭐⭐⭐', '5'),
    )

    image = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=250, default='Clothes')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    description = models.TextField(default='No description')
    size = models.CharField(
        max_length=12,  default='N/A')
    not_available = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, )
    stock = models.PositiveIntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, default='Category not available')
    Rating = models.CharField(
        default='⭐⭐⭐✰✰', max_length=20, choices=Rating_Choices)
    # Discounted Sales
    Discounted_Sales = models.BooleanField(default=False)
    Discounted_Price = models.DecimalField(
        decimal_places=2, default=0.00, max_digits=10)
    # Discounted Sales
    New_Arrival = models.BooleanField(default=False)

    def __str__(self):

        return self.name


class Cart(models.Model):
    Cart_Id = models.CharField(blank=True, max_length=250)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.Cart_Id


class Cart_Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def subtotal(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product.name


class User_FeedBack(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Subject = models.CharField(max_length=250)
    Message = models.TextField()

    def __str__(self):
        return f"{self.Name}: {self.Subject}"
