from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30, default='')
    last_name = models.CharField(max_length=30, default='')
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=5, decimal_places=2,null=True,blank=True)
    bio = models.TextField(null=True,blank=True)
    photo = models.ImageField(upload_to='', null=True, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
