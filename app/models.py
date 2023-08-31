from django.db import models

# Create your models here.

CATEGORY_CHOICES=(
    ('PL','Plastic'),
    ('DW', 'Disposable Wastes'),
    ('MT', 'Metal'),
)


class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    Category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')
    def __str__(self):
        return self.title
