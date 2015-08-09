# Create your views here.
from django.http import HttpResponse ,HttpResponseRedirect
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User
from survey.models import Survey,Question,Choice
from survey.forms import RegistrationForm ,CreateSurveyForm ,CreateQuestionForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
from survey_helper import validatechoices ,validatequestionform
import json

def index(request):
	context_dict={}
	return render(request,'survey/home.html', context_dict)
def about(request):
	return render(request,'survey/about.html')

def user_login(request):
	context_dict={}
	if request.method =='POST':
		print "inside post"
		print request.POST
		username = request.POST['username']
		password= request.POST['password']
		print username
		print password
		user = authenticate(username=username,password=password)
		print user 
		if user :
			if user.is_active:
				login(request,user)
				context_dict['msg']="successfully loggedin"
				return HttpResponseRedirect('/survey/')

			else:
				context_dict['msg']="user is not active pls contact support"
				

		else:
			context_dict['msg']="email or password combintion is incorrect"
			
		
		
	elif request.method =='GET':
		print "inside get"

	return render(request,'survey/login.html', context_dict)
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/survey/')
def answer_survey(request,survey_id):
	context_dict={}

	survey = Survey.objects.get(survey_id=survey_id)
	print survey
	print survey.survey_name
	print survey.questions
	
	context_dict['survey']=survey
	return render(request,'survey/answer_survey.html',context_dict)
def user_register(request):
	context_dict={}
	if request.method=='POST':
		print request.POST
		registration_form = RegistrationForm(request.POST)
		if registration_form.is_valid():
			registerd_user = registration_form.save()
			print registerd_user.password
			registerd_user.set_password(registerd_user.password)
			registerd_user.save()
			context_dict['msg']="successfully registered"
			user_login(request)
			return HttpResponseRedirect('/survey/')

		else:
			print registration_form.errors
			context_dict['msg']=registration_form.errors
			return render(request,'survey/register.html',context_dict)
	elif request.method=='GET': 
		return render(request,'survey/register.html',context_dict)
@login_required
def createsurvey(request):
	context_dict={}
	print request.method
	if request.method=='POST':
		print "******"
		print request.POST
		createsurvey_form=CreateSurveyForm(request.POST)
		if createsurvey_form.is_valid():
			survey = createsurvey_form.save()
			context_dict['msg']="success"
			survey.user=request.user
			survey.save()
			return redirect('create_question',survey.survey_id)
		else:
			 print createsurvey_form.errors
			 context_dict['msg']=createsurvey_form.errors
			 return render(request,'survey/create_survey.html',context_dict)
	elif request.method=='GET':
		return render(request,'survey/create_survey.html',context_dict)


@login_required
def create_question(request,survey_id):
	response_data = {}
	context_dict={}
	print "inside createquestion"
	if request.method=='POST':
		print "inside post"
		print request.POST
		print survey_id
		choicelist =request.POST.getlist('choice_label[]')
		createquestion_form=CreateQuestionForm(request.POST)
		response_data=validatequestionform(createquestion_form)
		if (not response_data['success']):
			print "inside failure "
			return  HttpResponse(json.dumps(response_data), content_type="application/json")
		response_data=validatechoices(choicelist)
		if (not response_data['success']):
			print "inside failure "
			return  HttpResponse(json.dumps(response_data), content_type="application/json")
		
		if createquestion_form.is_valid():
			question = createquestion_form.save()
			print question.question_description
			print Survey.objects.get(survey_id=survey_id)
			question.survey=Survey.objects.get(survey_id=survey_id)
			question.save()
			print question.survey

			for c in request.POST.getlist('choice_label[]'):
				choice_object = Choice(choice_description=c,choice_votes=0,question=question)
				try:
					choice_object.full_clean()
					choice_object.save()
				except ValidationError as e:
					print "inside ValidationError"
					print e.message_dict
					print e.message_dict['choice_description']
					constructmessage(False,'choice_description',"cannot be empty")
					response_data={'err' :e.message_dict }
					return HttpResponse(json.dumps(response_data), content_type="application/json")
			response_data={'success': True }
			print "before returning data "
			return HttpResponse(json.dumps(response_data), content_type="application/json")
		else:
			print createquestion_form.errors
			print dict(createquestion_form.errors.items())
			constructmessage(False,"question description",dict(createquestion_form.errors.items()))
			print response_data
			return HttpResponse(json.dumps(response_data), content_type="application/json")

		
	elif request.method=='GET':
		print "inside get"
		print survey_id
		context_dict['survey_id']=survey_id
		questions=Question.objects.filter(survey=Survey.objects.get(survey_id=survey_id))
		choices=[]
		for q in questions:
			choices.append(Choice.objects.filter(question=q))
		
		
		context_dict['questions']=questions
		context_dict['choices']=choices
		print context_dict['survey_id']
		return render(request,'survey/add_question.html',context_dict)





	return  HttpResponse('')

@login_required
def manage_survey(request):
	context_dict={}
	if request.method=='GET':
		print "inside get"
		surveylist=Survey.objects.filter(user=request.user)
		print surveylist
		context_dict['surveylist']=surveylist
		return render(request,'survey/manage_survey.html',context_dict)








