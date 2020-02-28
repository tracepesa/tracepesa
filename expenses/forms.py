from django import forms

from expenses.models import Expense, Category
from .fields import GroupedModelChoiceField


class ExpenseCategoriesForm(forms.ModelForm):
    category = GroupedModelChoiceField(
        queryset=Category.objects.exclude(parent=None),
        choices_groupby='parent'
    )

    class Meta:
        model = Expense
        fields = ('amount', 'description', 'category')


class AddExpenseForm(forms.ModelForm):
    amount = forms.DecimalField()

    class Meta:
        model = Expense
        fields = ['amount', 'description', 'category']
