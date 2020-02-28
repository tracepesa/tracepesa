from django.db import models

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)
    parent = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'


class Expense(models.Model):
    amount = models.DecimalField(max_digits=20, decimal_places=0)
    description = models.CharField(max_length=120, null=True, blank=True)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def get_absolute_url(self):
        return reverse('expense_update', kwargs={'pk': self.id})

    def __str__(self):
        return str(self.amount)
