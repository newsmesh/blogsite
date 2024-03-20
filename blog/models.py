from django.db import models

# Create your models here.


class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='media/', blank=True)
    img = models.BooleanField(default=False)
    title = models.CharField(max_length=200)
    discription = models.CharField(max_length=300)
    content = models.TextField(unique=True)
    slug = models.CharField(max_length=100)
    category = models.CharField(default='', null=True, max_length=50)
    imgtopic = models.CharField(default='', null=True, max_length=50)
    img_src = models.TextField(blank=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)
