from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title



class Product(models.Model):
    class Ratings(models.IntegerChoices):
        ZERO = 0
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    discount = models.FloatField(default=0)
    rating = models.IntegerField(choices=Ratings.choices, default=Ratings.ZERO.value)
    quantity = models.IntegerField(default=1)
    image = models.ImageField(upload_to='products/')
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')

    @property
    def discounted_price(self):
        if self.discount > 0:
            return self.price * (1 - self.discount / 100)
        return self.price

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name



class Order(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=150, default='N/A', blank=True)
    quantity = models.IntegerField(default=1)
    time = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='orders')

    def __str__(self):
        return self.name


class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    message = models.TextField()
    is_accessible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.name

