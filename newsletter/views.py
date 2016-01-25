from django.shortcuts import render
from .forms import SignUpForm, ContactForm		#L14, #L15

# Create your views here.
def home(request):
	title = 'Welcome'
	#if request.user.is_authenticated():		# to L13
	#	title = "My Title %s" % (request.user)	# to L13

	# if request.method == 'POST':				#L14 to L14
	# 	print request.POST						#L14 to L14

	form = SignUpForm(request.POST or None) 	#L14 - If there is request.POST data, then create an instance of form SignUpForm, if no data then don't

	context = {									#L13
		"title": title,							#L13
		"form": form,							#L14
	}


	if form.is_valid():
		instance = form.save(commit=False)		#L14 - Using this instead of just form.save() allows us to do something to the data before saving

		full_name = form.cleaned_data.get("full_name")
		if not full_name: 
			full_name = "New Full Name"
		instance.full_name = full_name

		instance.save()
		context = {
			"title": "Thank You"
		}

	return render(request, "home.html", context) #Render combines and returns (Request, Template, and Context)



def contact(request):							#L15
	form = ContactForm(request.POST or None)	#L15
	if form.is_valid():
		for key, value in form.cleaned_data.iteritems():
			print key, value
		# email = form.cleaned_data.get("email")
		# message = form.cleaned_data.get("message")
		# full_name = form.cleaned_data.get("full_name")
		# print email, message, full_name

	context = {									#L15
		"form": form,							#L15
	}											#L15
	return render(request, "forms.html", context) #L15