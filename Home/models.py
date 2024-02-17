from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=99)

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=180)
    price = models.DecimalField(max_digits=10, decimal_places=0, default=0, null=True)
    time_added = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    category = models.ManyToManyField(Category,)
    description = models.TextField()

    def __str__(self):
        return self.title
    
class BackgrounFigure(models.Model):
    title_1 = models.CharField(max_length=60)
    title_2 = models.CharField(max_length=60)
    image = models.ImageField(upload_to='background/')

    def __str__(self):
        return self.title_1

