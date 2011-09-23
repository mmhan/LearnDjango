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
        html= "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    else:
        now = datetime.datetime.now()
        html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)