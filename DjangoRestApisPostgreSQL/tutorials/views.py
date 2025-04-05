from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User  # Импорт модели User
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Income, Category, Expense
from django.core import serializers
import json


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class LoginView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }
        )


# @api_view(["GET", "POST", "DELETE"])
# def tutorial_list(request):
#     if request.method == "GET":
#         tutorials = Tutorial.objects.all()
#         tutorials_json = serializers.serialize("json", tutorials)
#         return JsonResponse(json.loads(tutorials_json), safe=False)
#
#     elif request.method == "POST":
#         data = json.loads(request.body)
#         tutorial = Tutorial(
#             title=data.get("title", ""),
#             description=data.get("description", ""),
#             published=data.get("published", False),
#         )
#         tutorial.save()
#         return JsonResponse(
#             {
#                 "id": tutorial.id,
#                 "title": tutorial.title,
#                 "description": tutorial.description,
#                 "published": tutorial.published,
#             },
#             status=status.HTTP_201_CREATED,
#         )
#
#     elif request.method == "DELETE":
#         Tutorial.objects.all().delete()
#         return JsonResponse(
#             {"message": "All tutorials were deleted successfully!"},
#             status=status.HTTP_204_NO_CONTENT,
#         )
#
#
# @api_view(["GET", "PUT", "DELETE"])
# def tutorial_detail(request, pk):
#     try:
#         tutorial = Tutorial.objects.get(pk=pk)
#     except Tutorial.DoesNotExist:
#         return JsonResponse(
#             {"message": "The tutorial does not exist"}, status=status.HTTP_404_NOT_FOUND
#         )
#
#     if request.method == "GET":
#         tutorial_json = serializers.serialize("json", [tutorial])
#         return JsonResponse(json.loads(tutorial_json)[0]["fields"], safe=False)
#
#     elif request.method == "PUT":
#         data = json.loads(request.body)
#         tutorial.title = data.get("title", tutorial.title)
#         tutorial.description = data.get("description", tutorial.description)
#         tutorial.published = data.get("published", tutorial.published)
#         tutorial.save()
#         return JsonResponse(
#             {
#                 "id": tutorial.id,
#                 "title": tutorial.title,
#                 "description": tutorial.description,
#                 "published": tutorial.published,
#             }
#         )
#
#     elif request.method == "DELETE":
#         tutorial.delete()
#         return JsonResponse(
#             {"message": "Tutorial was deleted successfully!"},
#             status=status.HTTP_204_NO_CONTENT,
#         )


# @api_view(["GET"])
# def tutorial_list_published(request):
#     tutorials = Tutorial.objects.filter(published=True)
#     tutorials_json = serializers.serialize("json", tutorials)
#     return JsonResponse(json.loads(tutorials_json), safe=False)


@api_view(["GET", "POST", "DELETE"])
def income_list(request):
    if request.method == "GET":
        incomes = Income.objects.all()
        incomes_json = serializers.serialize("json", incomes)
        return JsonResponse(json.loads(incomes_json), safe=False)

    elif request.method == "POST":
        data = json.loads(request.body)
        income = Income(
            amount=data.get("amount", 0),
            description=data.get("description", ""),
            date=data.get("date", ""),
        )
        income.save()
        return JsonResponse(
            {
                "id": income.id,
                "amount": float(income.amount),  # Decimal преобразуем в float для JSON
                "description": income.description,
                "date": income.date.isoformat(),  # Формат даты для JSON
                "created_at": income.created_at.isoformat(),
            },
            status=status.HTTP_201_CREATED,
        )

    elif request.method == "DELETE":
        Income.objects.all().delete()
        return JsonResponse(
            {"message": "All incomes were deleted successfully!"},
            status=status.HTTP_204_NO_CONTENT,
        )


@api_view(["GET", "PUT", "DELETE"])
def income_detail(request, pk):
    try:
        income = Income.objects.get(pk=pk)
    except Income.DoesNotExist:
        return JsonResponse(
            {"message": "The income does not exist"}, status=status.HTTP_404_NOT_FOUND
        )

    if request.method == "GET":
        income_json = serializers.serialize("json", [income])
        return JsonResponse(json.loads(income_json)[0]["fields"], safe=False)

    elif request.method == "PUT":
        data = json.loads(request.body)
        income.amount = data.get("amount", income.amount)
        income.description = data.get("description", income.description)
        income.date = data.get("date", income.date)
        income.save()
        return JsonResponse(
            {
                "id": income.id,
                "amount": float(income.amount),
                "description": income.description,
                "date": income.date.isoformat(),
                "created_at": income.created_at.isoformat(),
            }
        )

    elif request.method == "DELETE":
        income.delete()
        return JsonResponse(
            {"message": "Income was deleted successfully!"},
            status=status.HTTP_204_NO_CONTENT,
        )


@api_view(["GET", "POST", "DELETE"])
def expense_list(request):
    if request.method == "GET":
        expenses = Expense.objects.all()
        expenses_json = serializers.serialize("json", expenses)
        # Преобразуем в список словарей, чтобы включить поля category
        result = []
        for expense in json.loads(expenses_json):
            expense_fields = expense["fields"]
            expense_fields["id"] = expense["pk"]
            if expense_fields["category"]:
                category = Category.objects.get(id=expense_fields["category"])
                expense_fields["category"] = {"id": category.id, "name": category.name}
            else:
                expense_fields["category"] = None
            result.append(expense_fields)
        return JsonResponse(result, safe=False)

    elif request.method == "POST":
        data = json.loads(request.body)
        # Заглушка для ИИ: пока ставим категорию "Не определено" или null
        category, _ = Category.objects.get_or_create(name="Не определено")
        expense = Expense(
            amount=data.get("amount", 0),
            description=data.get("description", ""),
            date=data.get("date", ""),
            category=category,  # Заглушка вместо ИИ
        )
        expense.save()
        return JsonResponse(
            {
                "id": expense.id,
                "amount": float(expense.amount),
                "description": expense.description,
                "date": expense.date.isoformat(),
                "category": {"id": category.id, "name": category.name}
                if expense.category
                else None,
                "created_at": expense.created_at.isoformat(),
            },
            status=status.HTTP_201_CREATED,
        )

    elif request.method == "DELETE":
        Expense.objects.all().delete()
        return JsonResponse(
            {"message": "All expenses were deleted successfully!"},
            status=status.HTTP_204_NO_CONTENT,
        )


@api_view(["GET", "PUT", "DELETE"])
def expense_detail(request, pk):
    try:
        expense = Expense.objects.get(pk=pk)
    except Expense.DoesNotExist:
        return JsonResponse(
            {"message": "The expense does not exist"}, status=status.HTTP_404_NOT_FOUND
        )

    if request.method == "GET":
        expense_json = serializers.serialize("json", [expense])
        expense_data = json.loads(expense_json)[0]["fields"]
        expense_data["id"] = expense.id
        if expense.category:
            expense_data["category"] = {
                "id": expense.category.id,
                "name": expense.category.name,
            }
        else:
            expense_data["category"] = None
        return JsonResponse(expense_data, safe=False)

    elif request.method == "PUT":
        data = json.loads(request.body)
        expense.amount = data.get("amount", expense.amount)
        expense.description = data.get("description", expense.description)
        expense.date = data.get("date", expense.date)
        # Если передали категорию, можно обновить (пока без ИИ)
        if "category" in data and data["category"]:
            category, _ = Category.objects.get_or_create(name=data["category"]["name"])
            expense.category = category
        expense.save()
        return JsonResponse(
            {
                "id": expense.id,
                "amount": float(expense.amount),
                "description": expense.description,
                "date": expense.date.isoformat(),
                "category": {"id": expense.category.id, "name": expense.category.name}
                if expense.category
                else None,
                "created_at": expense.created_at.isoformat(),
            }
        )

    elif request.method == "DELETE":
        expense.delete()
        return JsonResponse(
            {"message": "Expense was deleted successfully!"},
            status=status.HTTP_204_NO_CONTENT,
        )
