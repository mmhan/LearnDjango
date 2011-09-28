from django.template import Context
from django.template.loader import get_template

from django.shortcuts import render_to_response

from django.http import HttpResponse, Http404
import datetime

def home(request):
    return HttpResponse("This is home!")

def hello(request):
    return HttpResponse("Hello World!")

def current_datetime(request, offset = 0):
    if offset != 0:
        try:
            offset = int(offset)
        except ValueError:
            raise Http404()
        dt = datetime.datetime.now() + datetime.timedelta(hours = offset)
        t = get_template('datetime.html')
        html= t.render(Context({'current_date' : dt, 'offset': offset}))
        return HttpResponse(html)
    else:
        now = datetime.datetime.now()
        return render_to_response('datetime.html', {'current_date': now, 'offset': offset}) #locals() is a useful function for this, a little risky