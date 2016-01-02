from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^about/$', views.About.as_view(), name='about'),
    url(r'^contact/$', views.Contact.as_view(), name='contact'),
    url(r'^resume/$', views.Resume.as_view(), name='resume'),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('blog.urls', namespace='blog')),
]