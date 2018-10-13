from django import forms

class meetingEnteryform(forms.Form):
	name = forms.CharField(max_length=100)
	date = forms.DateTimeField()
	description = forms.CharField(widget=forms.Textarea)
