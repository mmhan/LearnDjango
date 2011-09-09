from polls.models import Poll, Choice
from django.contrib import admin

class ChoiceInline(admin.TabularInline):
	'''
	This class is used to place choice into poll form.
	'''
	model = Choice
	extra = 3

class PollAdmin(admin.ModelAdmin):
	'''
	This defines the form for Poll
	'''
	#fields = ['pub_date', 'question']
	fieldsets = [
		(None,					{'fields': ['question']}),
		('Date Information',	{'fields': ['pub_date'], 
								 'classes': ['collapse']})
	]
	inlines = [ChoiceInline]
	
admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)