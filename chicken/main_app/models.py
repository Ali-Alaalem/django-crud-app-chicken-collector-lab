from django.db import models
from django.urls import reverse

SIZE = (
    ('S', 'Small'),
    ('M', 'Mid'),
    ('L', 'Large')
)

class Chicken(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    description = models.TextField(max_length=250)
  
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('chicken-detail', kwargs={'chicken_id': self.id})
    

class Eggs(models.Model):
    color = models.CharField(max_length=20)
    size = models.CharField(max_length=1,choices=SIZE,
        default=SIZE[0][0])
    
    chicken = models.ForeignKey(Chicken, on_delete=models.CASCADE)

    def __str__(self):
       return f"${self.size} and ${self.color}"