from django.shortcuts import render
from .forms import SignUpForm, ContactForm		#L14, #L15
from django.core.mail import send_mail			#L16
from django.conf import settings				#L16

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

	return render(request, "example_fluid.html", context) #Render combines and returns (Request, Template, and Context)



def contact(request):							#L15
	form = ContactForm(request.POST or None)	#L15
	if form.is_valid():
		# for key, value in form.cleaned_data.iteritems():
		# 	print key, value
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_full_name = form.cleaned_data.get("full_name")
		# print email, message, full_name

		subject = 'Site Contact Form'			#L16
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email, settings.EMAIL_HOST_USER]
		contact_message = "%s: %s via %s" %(
			form_full_name,
			form_message,
			form_email)
		
		some_html_message = """
		<h1>Hello</h1>
		"""

		send_mail(subject,						
			contact_message,
			from_email,
			[to_email],
			html_message=some_html_message,
			fail_silently=False) 				#L16

	context = {									#L15
		"form": form,							#L15
	}											#L15
	return render(request, "forms.html", context) #L15