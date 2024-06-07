
from django import forms
from .models import ExerciseSet, TrainingSession
from datetime import timedelta


class ExerciseSetForm(forms.ModelForm):
    rest_time = forms.DurationField(
        help_text="Enter rest time in format MM:SS"
    )

    class Meta:
        model = ExerciseSet
        fields = "__all__"

    def clean_rest_time(self):
        rest_time = self.cleaned_data['rest_time']
        if rest_time > timedelta(hours=1):
            raise forms.ValidationError(
                "Rest time should be less then 1 hous"
            )
        else:
            return rest_time
        
class TrainingSessionForm(forms.ModelForm):
    duration = forms.CharField(
        help_text="Enter training duration in format H:MM"
    )
    
    class Meta:
        model =  TrainingSession
        fields=  "__all__"

    def clean_duration(self):
        duration_str = self.cleaned_data['duration']
        try:
            hours , minutes = map( int , duration_str.split(":"))
            if  0 < hours > 8  or 0 < minutes > 60:
                raise ValueError
            else:
                duration = timedelta(hours = hours, minutes= minutes)
        except ValueError:
            raise forms.ValidationError(
                "Entered duration format was wrong. Type format H:MM"
            )
        return duration

    