from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    image = models.ImageField(
        upload_to='products',
    )


class Review(models.Model):
    CHOICE_1 = '1'
    CHOICE_2 = '2'
    CHOICE_3 = '3'
    CHOICE_4 = '4'
    CHOICE_5 = '5'

    CHOICES = (
        (1, CHOICE_1),
        (2, CHOICE_2),
        (3, CHOICE_3),
        (4, CHOICE_4),
        (5, CHOICE_5),
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.CharField(
        max_length=100,
        choices=CHOICES,
    )

    text = models.TextField(
        blank=True,
        null=True,
    )