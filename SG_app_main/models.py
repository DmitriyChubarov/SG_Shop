from django.db import models

class Tshirt(models.Model):
    Name = models.CharField(max_length=40)
    Photo = models.ImageField(upload_to='images/')
    Article = models.IntegerField()
    Size_S = models.CharField(max_length=5, default='0')
    Size_M = models.CharField(max_length=5, default='0')
    Size_L = models.CharField(max_length=5, default='0')
    Size_XL = models.CharField(max_length=5, default='0')
    Description = models.TextField()
    Price = models.IntegerField()
    Reserve_1 = models.TextField()
    Reserve_2 = models.TextField()
    Photo_reserve = models.ImageField()

    def __str__(self):
        return self.Name