from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
	url(r'^$', views.Home.as_view(), name='home'),
	url(r'^post/(?P<slug>[\w-]+)/$', views.PostDetailView.as_view(), name='post'),
	url(r'^tagged/(?P<slug>[\w-]+)/$', views.TaggedPostsListView.as_view(), name='tagged'),
	url(r'^subscribe/$', views.subscribe, name='subscribe')
]
