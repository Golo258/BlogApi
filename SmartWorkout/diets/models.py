from django.db import models


"""
    example_diet_type = {
        "name" : "vegetarian",
        "description" : "They dont' eat meat and animal products"
    }
"""


class DietType(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name


"""
    example_ingredient = 
    { 
        "name" : "Potato",
        "amount" : 200 (g)
        "proteins" : 12.5,       
        "carbs" : 8.5,       
        "fats" : 5.2,       
    }
"""


class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    # calories
    proteins = models.DecimalField(max_digits=5, decimal_places=2)
    carbs = models.DecimalField(max_digits=5, decimal_places=2)
    fats = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self) -> str:
        return self.name

    def get_calories_amount(self):
        return (self.proteins * 4 + self.carbs * 4 + self.fats * 9) * self.amount


"""
    example_meal = 
    { 
        "name" : "Scrumble Eggs",
        "ingredients" : [
            { 
            "name" : "Eggs",
            "amount" : 51,
            "proteins" : 12.5,       
            "carbs" : 8.5,       
            "fats" : 5.2,  
            },
              { 
            "name" : "Butter",
            "amount" : 15,
            "proteins" : 0.3,       
            "carbs" : 5.1,       
            "fats" : 21.5,  
            }
        ],
        "preparation_steps" : "Melt the butter in a pan and then add the eggs one by one"
    }
"""


class Meal(models.Model):
    name = models.CharField(max_length=60)
    ingredients = models.ManyToManyField(Ingredient, related_name="meals")
    preparation_steps = models.TextField()
    
    def __str__(self) -> str:
        return self.name

    def get_calories_total(self):
        total =0
        for ingredient in self.ingredients.all():
            total += ingredient.get_calories_amount()

        return total
            

"""
    example_recipe = {
        
    }
"""


