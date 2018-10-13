from django.shortcuts import render, get_object_or_404, redirect
from .models import Meeting
from.forms import meetingEnteryform
from django.http import HttpResponseRedirect 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

def index(request):
	return render(request, 'meetings/index.html')

def meetings(request):
	all_meetings = Meeting.objects.all()
	return render(request, 'meetings/meetings.html', {'meetings' : all_meetings})

def details(request, pk):
	meeting_details = Meeting.objects.get(id=pk)
	return render(request, 'meetings/details.html', {'meeting_details' : meeting_details})

def add(request):

	if request.method == 'POST':
		form = meetingEnteryform(request.POST)

		if form.is_valid():
			name = form.cleaned_data['name']
			date = form.cleaned_data['date']
			description = form.cleaned_data['description']

			Meeting.objects.create(
				name = name,
				date = date,
				description = description
			).save() 

			return HttpResponseRedirect('/meetings')
	else:
		form = meetingEnteryform()

	return render(request, 'meetings/form.html', {'form': form})


def delete(request, pk):
	
	record = get_object_or_404(Meeting, pk=pk)
	record.delete()

	return HttpResponseRedirect('/meetings')

def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)

		if form.is_valid():
			form.save()

			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect('/meetings')

	else:
		form = UserCreationForm()

	return render(request, 'registration/signup.html', {'form': form})