from django import forms
from .models import Data

class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['name','gender','age','hypertension',
                  'heart_disease','ever_married','work_type',
                  'residence_type','average_glucose_level','bmi',
                  'smoking_status']