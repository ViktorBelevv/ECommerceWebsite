from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

UserModel = get_user_model()


class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    image = models.ImageField(
        upload_to='products',
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=15)
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