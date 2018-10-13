from django.db import models

class Meeting(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	date = models.DateTimeField()
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "{name} @ {date}".format(name=self.name,date=self.date.strftime("%b-%d %H:%M"))
