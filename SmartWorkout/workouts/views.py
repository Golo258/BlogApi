
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models import Exercise
from .serializers import ExerciseSerializer

from drf_yasg.utils import swagger_auto_schema


class ExerciseViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['get'], url_path="all")
    def get_all_exercises(self, request:Request):
        queryset= Exercise.objects.all()
        serializer = ExerciseSerializer(
            instance = queryset, many = True
        )
        response = {
            "message" : "List of all created Exercises",
            "data" : serializer.data
        }
        return Response(
            data = response, status= status.HTTP_200_OK
        )
    @action(detail=True, methods=['get'], url_path="retrieve")
    def get_exercise_by_id(self, request:Request, pk = None):
        exercise = get_object_or_404(Exercise, pk= pk)
        serializer = ExerciseSerializer(instance=exercise)
        response = {
            "message" : f"Exercise by its id: {pk}",
            "data" : serializer.data
        }
        return Response(
            data = response, status= status.HTTP_200_OK
        )

    @swagger_auto_schema(request_body=ExerciseSerializer)
    @action(detail=False, methods=['post'], url_path="create")
    def create_new_exercise(self, request: Request):
        serializer = ExerciseSerializer(data= request.data)

        if serializer.is_valid():
            serializer.save()
            response = {
                "message" : f"New Exercise {serializer.data['name']} has been created",
                "data" : serializer.data
            }
            return Response(data= response, status= status.HTTP_201_CREATED)
        else:
            response  = {
                "message" : "The request body is not valid",
                "data" : serializer.errors
            
            }
            return Response(data= response, status= status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=ExerciseSerializer)
    @action(detail=True, methods=['put'], url_path="update")
    def update_exercise_by_id(self, request: Request, pk=None):
        exercise = get_object_or_404(Exercise, pk = pk)
        serializer  = ExerciseSerializer(instance= exercise,
                                         data = request.data,
                                         partial = True)
        
        if serializer.is_valid():
            serializer.save()
            response = {
                "message" : f"Exercise {exercise['name']} has been updated",
                "data" : serializer.data
            }
            return Response(data= response, status= status.HTTP_200_OK)
        else:
            response  = {
                "message" : "The request body is not valid",
                "data" : serializer.errors
            }
            return Response(data= response, status= status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['delete'], url_path="remove")
    def remove_exercise(self, request:Request, pk=None):
        exercise = get_object_or_404(Exercise, pk = pk)
        exercise.delete()
        response = {
                "message" : f"Exercise {exercise['name']} has been deleted",
            }
        return Response(data= response, status= status.HTTP_204_NO_CONTENT)