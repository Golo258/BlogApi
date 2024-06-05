from django.contrib import admin

from .models import  (
Exercise, ExerciseSet, WorkoutType, SetType,TrainingSession,

)

admin.site.register(WorkoutType)
admin.site.register(SetType)


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', ]
    list_filter =['equipment','muscle_group']



@admin.register(ExerciseSet)
class ExerciseSetAdmin(admin.ModelAdmin):
    list_display = ['used_volume', 'repetitions_number', 'rest_time']
    list_filter =['used_volume']


@admin.register(TrainingSession)
class TrainingSessionAdmin(admin.ModelAdmin):
    list_display = ['notes', 'series_amount', 'training_number']
    list_filter =['date']
