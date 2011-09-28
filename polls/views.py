from polls.models import Poll
from django.shortcuts import render_to_response, HttpResponse

def index(request):
	latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
	return render_to_response('polls/index.html', {'latest_poll_list' : latest_poll_list})
	
def detail(request, poll_id):
	return HttpResponse("This is the detail view for %s" % poll_id)
	
def results(request, poll_id):
	return HttpResponse("This is the results view for %s" % poll_id )
	
def vote(request, poll_id):
	return HttpResponse("This is the vote view for %s" % poll_id)