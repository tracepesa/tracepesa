from django.contrib import admin

# Register your models here.
from expenses.models import Expense, Category

admin.site.register(Expense)
admin.site.register(Category)
