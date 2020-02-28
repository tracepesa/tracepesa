"""tracepesa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from expenses.views import HomeListView, ExpenseUpdateView, ExpenseDeleteView, ExpenseDetailView, ExpenseSearchView, \
    add_expense

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeListView.as_view(), name='homepage'),
    path('expense/add', add_expense, name='expense_add'),
    path('expense/<int:pk>/detail', ExpenseDetailView.as_view(), name='expense_detail'),
    path('expense/<int:pk>/update', ExpenseUpdateView.as_view(), name='expense_update'),
    path('expense/<int:pk>/delete', ExpenseDeleteView.as_view(), name='expense_delete'),
    path('expense/search', ExpenseSearchView.as_view(), name='expense_search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
