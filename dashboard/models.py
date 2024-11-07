from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from sklearn.tree import DecisionTreeClassifier
import joblib
# Create your models here.
GENDER_CHOICES = (
    (0, 'Female'),
    (1, 'Male'),
    (2, 'Other')
)
HYPERTENSION_CHOICES = (
    (0, 'No Hypertension'),
    (1, 'Hypertension')
)
HEART_DISEASE_CHOICES=(
    (0,'No Heart disease'),
    (1,'heart disease')
)
EVER_MARRIED_CHOICES = (
    (0,'Never Married'),
    (1,'married')
)
WORK_TYPE_CHOICES = (
    (0,'Private Sector'),
    (1,'Self Employed'),
    (2,'Public Sector'),
    (3,'Home Maker'),
    (4,'Never Worked')
)
RESIDENCE_CHOICES = (
    (0,'Urban'),
    (1,'Rural')
)
SMOKING_STATUS_CHOICES = (
    (0,'Formerly Smoked'),
    (1,'Never Smoked'),
    (2,'Smoke'),
    (3,'Unknown')
)
STROKE_CHOICES = (
    (0,'No Stroke'),
    (1,'Stroke')
)
class Data(models.Model):
    name = models.CharField(max_length=50,null=True,)
    gender = models.PositiveIntegerField(null=True, choices=GENDER_CHOICES)
    age = models.IntegerField(
        validators= [MinValueValidator(10), MaxValueValidator(100)],null=True)
    hypertension = models.PositiveIntegerField(null=True, choices=HYPERTENSION_CHOICES)
    heart_disease = models.PositiveIntegerField(null=True, choices=HEART_DISEASE_CHOICES)
    ever_married = models.PositiveIntegerField(null=True, choices=EVER_MARRIED_CHOICES)
    work_type = models.PositiveIntegerField(null=True, choices=WORK_TYPE_CHOICES)
    residence_type = models.PositiveIntegerField(null=True, choices=RESIDENCE_CHOICES)
    average_glucose_level = models.IntegerField(null=True,)
    bmi = models.IntegerField(null=True)
    smoking_status = models.PositiveIntegerField(null=True, choices=SMOKING_STATUS_CHOICES)
    stroke_predictions = models.PositiveIntegerField(blank=True, choices=STROKE_CHOICES,null=True)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        ml_model =joblib.load('ml_model/ml_stroke_predictor.joblib')
        self.stroke_predictions = ml_model.predict([[self.gender,self.age,
                           self.hypertension,self.heart_disease,
                           self.ever_married,self.work_type,
                           self.residence_type,self.average_glucose_level,
                           self.bmi,self.smoking_status]])
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name

