from datetime import timedelta, date

from django.db import models
from users.models import (User, unregistered_users)
from products.models import products_combinations


""" all the items in a single order of a registered user"""
class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                           related_name="order_item_user")
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(products_combinations, on_delete=models.CASCADE,
                             related_name="item")
    quantity = models.IntegerField(default=1)
    delivered = models.BooleanField(default=False)
    cancelled = models.BooleanField(default=False)

    def __str__(self):
        return (self.item.combination_string+"," +str(self.quantity))


""" order created by a registered user """
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="order_user")
    ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem, related_name="OrderItem")
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    delivered = models.BooleanField(default=False)

    def __str__(self):
        return (self.user.email + str(self.start_date))

    def save(self,*args,**kwargs):
        """ this must be changed according to business need"""
        end_date = date.today() + timedelta(days=3)
        self.ordered_date = end_date
        super().save(*args, **kwargs)


""" order item for each order by unregistered user """
class UnregisteredOrderItem(models.Model):
    user = models.ForeignKey(unregistered_users, on_delete=models.CASCADE,
                             related_name="order_item_unregistereduser")
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(products_combinations, on_delete=models.CASCADE,
                             related_name="unregister_item")
    quantity = models.IntegerField(default=1)
    delivered = models.BooleanField(default=False)

    def __str__(self):
        return (self.item.combination_string+","+str(self.quantity))


""" order created by an uregistered user """
class UnregisteredOrder(models.Model):
    user = models.ForeignKey(unregistered_users, on_delete=models.CASCADE,
                             related_name="order_unregistereduser")
    ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(UnregisteredOrderItem,
                                   related_name="unregister_OrderItem")
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    delivered = models.BooleanField(default=False)

    def __str__(self):
        return (self.user.email+str(self.start_date))

    def save(self,*args,**kwargs):
        """ this must be changed according to business need"""
        EndDate = date.today() + timedelta(days=3)
        self.ordered_date = EndDate
        super().save(*args, **kwargs)