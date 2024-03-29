from django.conf.urls.defaults import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'views.home'),
	(r'^hello/$', 'views.hello'),
	(r'^time/$', 'views.current_datetime'),
	(r'^time/plus/(\d{1,2})/$', 'views.current_datetime'),
	(r'^polls/$', 'polls.views.index'),
	(r'^polls/(?P<poll_id>\d+)/$', 'polls.views.detail'),
	(r'^polls/(?P<poll_id>\d+)/results/$', 'polls.views.results'),
	(r'^polls/(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
	
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
