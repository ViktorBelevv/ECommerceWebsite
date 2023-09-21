from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    image = models.ImageField(
        upload_to='products',
    )


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.CharField(
        max_length=100,
        validators=[
            MinValueValidator('1'),
            MaxValueValidator('5'),
        ]
    )

    text = models.TextField(
        blank=True,
        null=True,
    )