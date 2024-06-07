
from django.db import models


'''
    Type example:
    Split / FBW / Calisthenic etc
'''
class WorkoutType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    target = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

class SetType(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()

'''
    Set example:
        used_volume: 60kg
        repetions_number: 12 
        rest_time: 3 minutes 20 seconds
        is_spotted: True
        Tempo: 3 - 2 - 1
        SetType:
            name: Failure:
            description: I was a bit tired at this Set
'''

class ExerciseSet(models.Model):
    used_volume = models.DecimalField(max_digits=5, decimal_places=2)
    repetitions_number = models.IntegerField()
    rest_time = models.DurationField()
    is_spotted = models.BooleanField(default=False)
    tempo = models.CharField(max_length=10)
    set_type = models.ForeignKey(
        SetType, on_delete=models.CASCADE, related_name="sets"
    )

    def __str__(self):
        return f"Set < {self.repetitions_number} x {self.used_volume} kg"

'''
    Exercise Example:
        name: Bench Press
        description: Lay down on a bench and get the barbell with weight .....
        equipment : Barbell
        muscle_group: Chest
'''
class Exercise(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    equipment = models.CharField(max_length=50)
    muscle_group = models.CharField(max_length=60)
    sets = models.ManyToManyField(
        ExerciseSet, related_name="exercises"
    )
    def __str__(self):
        return self.name

'''
    Session example:
        date = 2024-07-12
        duration: 2h 15 minute
        series_amount: 15 series
        training_number: 150
        workout_type : FBW
        Exercises: <Exercise1> <Exercise2, Exercise3>
'''
class TrainingSession(models.Model):
    date = models.DateField()
    notes = models.TextField()
    duration = models.DurationField()
    series_amount = models.IntegerField()
    training_number = models.IntegerField()
    workout_type = models.ForeignKey(
        WorkoutType, on_delete=models.CASCADE, related_name="sessions"
    )
    exercises = models.ManyToManyField(
        Exercise, related_name="sessions"
    )

    def __str__(self):
        return self.notes



'''
    Consider later 
'''
# class Achievement(models.Model):
#     title = models.CharField()
#     description = models.TextField()
