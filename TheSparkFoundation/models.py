from django.db import models

# Create your models here.

class Customers(models.Model):
    Name  = models.CharField(max_length=50,default='')
    Email = models.EmailField(max_length=250,default='none@none.com')
    Current_Balance = models.CharField(max_length=100, default=0)
    Account_Number = models.CharField(max_length=50,default='123456789')
    Phone_Number = models.CharField(max_length=10,default='9999999999')
    IFSC_Code = models.CharField(max_length=50,default='FR1234567890')
    Address = models.CharField(max_length=150,default='abcd')
    Branch_Code = models.CharField(max_length=20,default='023F')

    def __str__(self):
        return self.Name+" | "+self.Email