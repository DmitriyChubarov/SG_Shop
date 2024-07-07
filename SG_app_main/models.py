from django.db import models

class Tshirt(models.Model):
    Name = models.CharField(max_length=40)
    Photo = models.ImageField(upload_to='images/')
    Article = models.IntegerField()
    Size = models.CharField(max_length=5)
    Description = models.TextField()
    Price = models.IntegerField()
    Reserve_1 = models.TextField()
    Reserve_2 = models.TextField()
    Photo_reserve = models.ImageField()

    def __str__(self):
        return self.Name