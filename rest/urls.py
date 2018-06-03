from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
urlpatterns = [
	
	url(r'^book/$', views.AvailableBooksList.as_view()),
	url(r'^single/(?P<pk>[0-9]+)$', views.AvailableBooksDetail.as_view()),
    
	]

urlpatterns = format_suffix_patterns(urlpatterns)