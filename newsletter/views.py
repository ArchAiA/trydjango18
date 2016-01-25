from django.shortcuts import render

# Create your views here.
def home(request):
	title = 'Welcome'
	if request.user.is_authenticated():
		title = "My Title %s" % (request.user)
	
	context = {
		"template_title": title,
		}

	return render(request, "home.html", context) #Render comibines and returns (Request, Template, and Context)