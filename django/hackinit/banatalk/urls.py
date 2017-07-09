from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^chatroom/$',views.chatroom, name='chatroom'),
    url(r'^stat/$',views.stat, name='stat'),
    url(r'^addimg/$',views.addimg, name='addimg'),
]
