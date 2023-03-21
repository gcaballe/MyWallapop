from django.db import models

# Create your models here.
    
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    avatar = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    price = models.FloatField()
    description = models.CharField(max_length=300)
    image = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def getComments(self):
        return Comment.objects.filter(product=self.id).all()

    def __str__(self):
        return self.name
    

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    text = models.CharField(max_length=100)