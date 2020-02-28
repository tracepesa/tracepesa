from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from expenses.forms import AddExpenseForm, ExpenseCategoriesForm
from expenses.models import Expense


class HomeListView(ListView):
    model = Expense
    template_name = 'expenses/homepage.html'
    context_object_name = 'expenses'
    ordering = ['-date_created']
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AddExpenseForm()
        return context


class ExpenseSearchView(ListView):
    model = Expense
    template_name = 'expenses/expense_search.html'
    context_object_name = 'expenses'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('query')
        return context

    def get_queryset(self):
        return Expense.objects.filter(description__icontains=self.request.GET.get('query')).order_by(
            '-date_created') | Expense.objects.filter(amount__icontains=self.request.GET.get('query')).order_by(
            '-date_created') | Expense.objects.filter(category__name__icontains=self.request.GET.get('query')).order_by(
            '-date_created')


class ExpenseDetailView(DetailView):
    model = Expense

    template_name = 'expenses/expense_detail.html'
    context_object_name = 'expense'


class ExpenseUpdateView(UpdateView):
    model = Expense
    template_name = 'expenses/expense_update.html'
    fields = ['amount', 'description']
    success_url = '/'


class ExpenseDeleteView(DeleteView):
    model = Expense
    success_url = '/'
    template_name = 'expenses/expense_delete_confirm'
    context_object_name = 'expense'


class ExpenseCreateView(CreateView):
    model = Expense
    fields = ['amount', 'description']


def add_expense(request):
    if request.method == 'POST':
        form = AddExpenseForm(request.POST)
        categories_form = ExpenseCategoriesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
        else:
            print('Form not valid')
    else:
        form = AddExpenseForm()
        # categories_form = ExpenseCategoriesForm()
        context = {"form": form}
        return render(request, 'expenses/expense_add.html', context)

    return redirect('homepage')
