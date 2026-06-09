from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField (max_digits=10, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='cars_images/', blank=True, null=True)
    def __str__(self):
        return self.name