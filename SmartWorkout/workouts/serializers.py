
from rest_framework import serializers
from .models import Exercise, ExerciseSet


class ExerciseSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseSet
        fields = "__all__"



class ExerciseSerializer(serializers.ModelSerializer):
    sets = ExerciseSetSerializer(many=True)

    class Meta:
        model = Exercise
        fields = "__all__"

    
    def create(self, validated_data):
        sets_data = validated_data.pop("sets")
        exercise = Exercise.objects.create(**validated_data)
        for set_data in sets_data:
            ExerciseSet.objects.create(
                exercise = exercise, **set_data
            )
        return exercise