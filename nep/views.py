from django.shortcuts import render
from django.core.exceptions import ValidationError
from .forms import SignupForm, LoginForm, ContactsForm
from .models import User
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
# Create your views here.
def indexView(request):
	return render(request, 'index.html')

def aboutView(request):
	return render(request, 'about.html')

def blogView(request, uname='satou.M'):
	user = User.objects.get(username=uname)
	context = {'user':user}
	return render(request, 'blog.html', context)

def contactsView(request):
	if request.method == 'POST':
		form = ContactsForm(request.POST)
		if form.is_valid():
			sender = form.cleaned_data['email']
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			recipient = ['kylepagayon58@gmail.com']

			message = "From: "+sender+"\n"+message

			try:
				send_mail(subject, message, sender, recipient, fail_silently=True)

			except BadHeaderError:
				return HttpResponse('Invalid Header Found.')
				message.success(request, "Your response has been submited successfully.")

			form = ContactsForm()

	form = ContactsForm()
	context = {'form':form}
	return render(request, 'contacts.html', context)
	
def nepgear_secret_site(request):
	return render(request, 'nepgear_secret_site.html')


def signupView(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			password1 = form.cleaned_data['password1']
			password2 = form.cleaned_data['password2']
			if password1 == password2:
				user = User.objects.create(username=form.cleaned_data['username'],
					password=form.cleaned_data['password1'], email=form.cleaned_data['email'])
				user.save()
				form = SignupForm()

			else:
				raise ValidationError('Passwords don\'t match')

	form = SignupForm()
				
	context = {'form':form}
	return render(request, 'registrations/signup.html', context)

def loginView(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			uname = form.cleaned_data['username']
			passwd = form.cleaned_data['password']
			if uname == 'nepgya' and passwd == 'nepgya':
				return nepgear_secret_site(request)
			if User.objects.get(username=uname) and User.objects.get(password=passwd):
				return blogView(request, uname)




			else:
				raise ValidationError('Incorrect Username and Password.')


	form = LoginForm()
	context = {'form':form}
	return render(request, 'registrations/login.html', context)
