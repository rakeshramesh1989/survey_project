from django import forms
from django.contrib.auth.models import User
from survey.models import Survey , Question


class RegistrationForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields=('first_name','last_name','username','email','password')


class CreateSurveyForm(forms.ModelForm):
	class Meta:
		model = Survey
		fields =('survey_name','survey_description')

class CreateQuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields =('question_description',)

