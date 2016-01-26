from django.shortcuts import render

# Create your views here.
def about(request):

	context = {}
	return render(request, "about.html", context) #Render combines and returns (Request, Template, and Context)
