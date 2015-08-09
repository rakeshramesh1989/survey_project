from django.conf.urls import url,patterns
from survey import views

urlpatterns = patterns('',url(r'^$', views.index, name='index'),
						  url(r'^about/$',views.about,name='about'),
						  url(r'^login/$', views.user_login, name='user_login'),
						  url(r'^register/$', views.user_register, name='user_register'),
						  url(r'^logout/$',views.user_logout,name='logout'),
						  url(r'^create_survey/$',views.createsurvey,name='createsurvey'),
						  url(r'^manage_survey/$',views.manage_survey,name='manage_survey'),
						  url(r'^create_question/(?P<survey_id>[\w\-]+)/$',views.create_question,name='create_question'),
						  url(r'^answer_survey/(?P<survey_id>[\w\-]+)/$',views.answer_survey,name='answer_survey'),
					  )