from django.conf.urls import url
from . import views
from . import views as core_views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^index.html$', views.post_list, name='index'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name="post_edit"),
    url(r'^signup/$', core_views.signup, name='signup'),
]
