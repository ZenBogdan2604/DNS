from django.db import models

class Tovar(models.Model):
    title = models.CharField(max_length=50)
    descpription = models.CharField(max_length=200)
    price = models.FloatField()
    def __str__(self):
        return self.title

class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    def __str__(self):
        return self.name

class Zakaz(models.Model):
    title = models.CharField(max_length=100)
    tovar = models.ForeignKey(Tovar, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
