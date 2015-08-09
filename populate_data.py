import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','survey_project.settings')
from django.contrib.auth.models import User
from survey.models import Survey,Question,Choice

def populate():

	user_object = create_user(user_name='rameshrakeshtest1',first_name='rakesh',last_name='rameshtest1',user_email='rakeshr.msec+test1@gmail.com',user_password='June@2012')
	choice_list= [create_choice(choice_id=1,choice_description='test chice1',choice_votes=0),create_choice(choice_id=2,choice_description='test chice2',choice_votes=0)]
	choice_list2= [create_choice(choice_id=3,choice_description='test chice1',choice_votes=0),create_choice(choice_id=4,choice_description='test chice2',choice_votes=0)]
	questionlist =[create_question(question_id=1,question_description='testquestion',question_choiceslist=choice_list),create_question(question_id=2,question_description='testquestion2',question_choiceslist=choice_list2)]

	survey_object =create_survery(survey_id=1,survey_name="survey on  film industry ",survey_description="This is the simple survey to get info about differnt film industry in india",user=user_object,questions=questionlist)
    
	for s in Survey.objects.all():
		for q in Question.objects.all():
			print "- {0} - {1}".format(str(s.survey_name), str(q.question_description))
			for c in Choice.objects.all():
				print "- {0} - {1}".format(str(q.question_description), str(c.choice_description))



def create_user(user_name,first_name,last_name,user_email,user_password):
	print "inside create user"
	u = User.objects.get_or_create(email=user_email)[0]
	u.first_name = first_name
	u.last_name = last_name
	u.email = user_email
	u.set_password(user_password)
	u.username = user_name
	u.save()
	print u
	print "after create user "
	

	return u
def create_survery(survey_id,survey_name,survey_description,user,questions):
	print "** inside survey"
	print survey_id
	print user.username
	print user.email
	print user.password
	s = Survey.objects.get_or_create(survey_id=survey_id)[0]
	print "inside exec"
	print "after getting survey"
	print s
	s.user = user 
	s.survey_id=survey_id
	s.survey_name=survey_name
	s.survey_description=survey_description
	s.questions = questions
	print "***** user object "
	print user
	s.save()
	return s
def create_question(question_id,question_description,question_choiceslist):
	q = Question.objects.get_or_create(question_id=question_id)[0]
	q.question_id=question_id
	q.question_description=question_description
	q.question_choices=question_choiceslist
	q.save()
	return q
def create_choice(choice_id,choice_description,choice_votes):
	c = Choice.objects.get_or_create(choice_id=choice_id)[0]
	c.choice_id = choice_id
	c.choice_description = choice_description
	c.choice_votes = choice_votes
	c.save()
	return c

if __name__ == '__main__':
    print "Starting Survey population script..."
    populate()

