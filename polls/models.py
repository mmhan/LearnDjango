from django.db import models

# Create your models here.
class Poll(models.Model):
	'''
	This is the poll model
	'''
	question = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	
	def __unicode__(self):
		'''
		customizing inspection
		'''
		return self.question
	
class Choice(models.Model):
	'''
	This is the answer choice model
	'''
	poll = models.ForeignKey(Poll)
	choice = models.CharField(max_length=200)
	votes = models.IntegerField()
	
	def __unicode__(self):
		'''
		customizing inspection
		'''
		return self.choice
	