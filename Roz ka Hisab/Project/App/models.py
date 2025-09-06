from django.db import models

# Create your models here.
class FamilyMembers(models.Model):
    name=models.CharField(max_length=100,unique=True)
    photo=models.ImageField(upload_to='photo',default='user.png')

    def __str__(self):
        return self.name


class Expense(models.Model):
    member=models.ForeignKey(FamilyMembers,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.CharField(choices=[
        ("Food", "Food"),
        ("Travel", "Travel"),
        ("Shopping", "Shopping"),
        ("Bills", "Bills"),
        ("Toys", "Toys"),
        ("Medicine", "Medicine"),
        ("Fees", "Fees"),
    ])

    date=models.DateField(auto_now_add=True)
    time=models.TimeField(auto_now_add=True)
    note=models.TextField(blank=True,null=True)
