from django.db import models
from django.contrib.auth import get_user_model
user= get_user_model ()

class cpurchase(models.Model):
    user=models.ForeignKey(user,on_delete=models.CASCADE,null=True)
    date=models.TextField(null=True)
    status=models.TextField(null=True)
    duedate=models.TextField(null=True)
    order=models.TextField(null=True)
    vendor=models.TextField(null=True)
    total=models.TextField(null=True)
    filters=models.TextField(null=True)
    Sfilters=models.TextField(null=True)

class userdata(models.Model):
    user=models.ForeignKey(user,on_delete=models.CASCADE,null=True)
    vendor=models.TextField(max_length=255)

class orderno(models.Model):
    user=models.ForeignKey(user,on_delete=models.CASCADE,null=True)
    ordernumber=models.TextField(default="PO001")
