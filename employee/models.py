 
 
 

# Create your models here.


from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address=models.CharField(max_length=60)
    image = models.ImageField(upload_to='employee_images/', null=True, blank=True) 
    department=models.CharField(max_length=25)
    salary=models.DecimalField(max_digits=10,decimal_places=4)
    joined_date=models.DateField(auto_now_add=True)

    def __str__(self):
     return self.name