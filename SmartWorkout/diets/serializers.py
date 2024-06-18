from rest_framework.serializers import ModelSerializer
from .models import DietType, Ingredient, Meal


class DietTypeSerializer(ModelSerializer):

    class Meta:
        model = DietType
        fields = ["name", "description"]


class IngredientSerializer(ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ["name", "amount", "proteins", "carbs", "fats"]

    

class MealSerializer(ModelSerializer):
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Meal
        fields = "__all__"

    
    def create(self, validated_data):
        ingredients_data = validated_data.pop("ingredients")
        ingredient = Ingredient.objects.create(**validated_data)
        for data in ingredients_data:
            Ingredient.objects.create(
                exercise = ingredient, **data
            )
        return ingredient
    
    def get_calories_total(self, object):
        return object.get_calories_total()