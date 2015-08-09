import json
def validatequestionform(createquestion_form):
	if createquestion_form.is_valid():

		return constructmessage(True,''," ")
	else:
		 return constructmessage(False,'question_description',"cannot be empty")

def validatechoices(choicelist):
	print "inside validatechoices"
	if len(choicelist)==0:

		return constructmessage(False,"choicedescription","cannot be empty ")
	else:

		for c in choicelist:
			if c:
					print "element found  "
			else:

				print "element not  found "
				return constructmessage(False,"choicedescription"," cannot be empty ")

	return constructmessage(True,"","")



def constructmessage(success,field_name,errormessage):
	response_data={}
	if success:
		response_data={'success': True }
	else:
		response_data={'success': False }
		response_data['err'] =field_name+" "+errormessage 
		
		json_data = json.dumps(response_data)
		print response_data
		
		
	return response_data
	










