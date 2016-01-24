from django.contrib import admin
from .models import SignUp #import from the same folder from the models file
from .forms import SignUpForm #For using ModelForms
# Register your models here.



class SignUpAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "timestamp", "updated"]
	form = SignUpForm
	#class Meta: #Replaced With ModelForm
	#	model = SignUp #Replaced With ModelForm




admin.site.register(SignUp, SignUpAdmin)
