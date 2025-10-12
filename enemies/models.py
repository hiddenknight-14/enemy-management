from django.db import models

# Create your models here.=True

class Enemy(models.Model):
    name = models.CharField(max_length=100)
    reason = models.CharField(max_length=1000)
    revenge_taken = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='images', blank=True, default="images/image.png")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name