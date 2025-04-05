from django.urls import path
from .views import (
    RegisterView,
    LoginView,
    income_list,
    income_detail,
    expense_list,
    expense_detail,
)

urlpatterns = [
    path("api/auth/register/", RegisterView.as_view(), name="register"),
    path("api/auth/login/", LoginView.as_view(), name="login"),
    path("api/incomes/", income_list, name="income-list"),
    path("api/incomes/<int:pk>/", income_detail, name="income-detail"),
    path("expenses/", expense_list, name="expense-list"),
    path("expenses/<int:pk>/", expense_detail, name="expense-detail"),
]
