from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_204_NO_CONTENT,
)
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404


from .models import Ingredient, Meal
from .serializers import IngredientSerializer, MealSerializer

from drf_yasg.utils import swagger_auto_schema


class IngredientViewSet(viewsets.ViewSet):

    @action(detail=False, methods=["get"], url_path="all_ingredients")
    def get_all_ingredients(self, request: Request):
        queryset = Ingredient.objects.all()
        serializer = IngredientSerializer(instance=queryset, many=True)
        response_data = {"message": "List of all ingredients", "data": serializer.data}
        return Response(data=response_data, status=HTTP_200_OK)

    @action(detail=True, methods=["get"], url_name="grab_ingredient")
    def get_ingredient_by_id(self, request: Request, pk=None):
        ingredient = get_object_or_404(Ingredient, pk=pk)
        serializer = IngredientSerializer(instance=ingredient)
        response_data = {"message": f"Ingredient by id: {pk}", "data": serializer.data}
        return Response(data=response_data, status=HTTP_200_OK)

    @swagger_auto_schema(request_body=IngredientSerializer)
    @action(detail=False, methods=["post"], url_path="create_ingredient")
    def create_new_ingredient(self, request: Request):
        serializer = IngredientSerializer(data=request.data)
        if serializer.is_valid():
            response_data = {
                "message": f"New Ingredient: {serializer.data['name']} has been created",
                "data": serializer.data,
            }
            return Response(data=response_data, status=HTTP_201_CREATED)

        else:
            response_data = {
                "message": "The request body is not valid",
                "data": serializer.errors,
            }
            return Response(data=response_data, status=HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=IngredientSerializer)
    @action(detail=False, methods=["put"], url_path="create_ingredient")
    def update_existing_ingredient(self, request: Request, pk=None):
        ingredient = get_object_or_404(Ingredient, pk=pk)
        serializer = IngredientSerializer(
            instance=ingredient, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            response_data = {
                "message": f"Ingredient with: {serializer.data['name']} has been updated",
                "data": serializer.data,
            }
            return Response(data=response_data, status=HTTP_201_CREATED)

        else:
            response_data = {
                "message": "The request body is not valid",
                "data": serializer.errors,
            }
            return Response(data=response_data, status=HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["delete"], url_path="remove_ingredient")
    def remove_exercise(self, request: Request, pk=None):
        ingredient = get_object_or_404(Ingredient, pk=pk)
        ingredient.delete()
        response_data = {
            "message": f"Ingredient {ingredient['name']} has been deleted",
        }
        return Response(data=response_data, status=HTTP_204_NO_CONTENT)
