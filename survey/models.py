from django.db import models
from django.contrib.auth.models import User
from djangotoolbox.fields import ListField
from djangotoolbox.fields import EmbeddedModelField

# Create your models here.

class Survey(models.Model):
	survey_id=models.AutoField(primary_key=True)
	survey_name=models.CharField(max_length=100,null=True)
	survey_description = models.TextField(null=True)
	user = models.ForeignKey('auth.User',null=True)
	#questions = ListField(EmbeddedModelField('Question'),null=True)

class Question(models.Model):
	question_id=models.AutoField(primary_key=True)
	question_description=models.CharField(max_length=100)
	#question_choices = ListField(EmbeddedModelField('Choice'),null=True)
	survey = models.ForeignKey('Survey',null=True)
	

class Choice(models.Model):
	choice_id=models.AutoField(primary_key=True)
	choice_description = models.CharField(max_length=100)
	choice_votes = models.IntegerField(default=0)
	question = models.ForeignKey('Question',null=True)


	

