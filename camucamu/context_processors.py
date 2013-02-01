import datetime

def loggedstatus(request):
	if request.user.is_authenticated():
		return {
			'logged_in' : True
		}
	else:
		return {
			'logged_in' : False
		}

def now(request):
	return {
		'current_date' : datetime.datetime.now()
		}
