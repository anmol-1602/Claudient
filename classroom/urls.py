from django.conf.urls import url

from . import views
app_name='classroom'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/$',views.signup,name='signup'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^doubts/$',views.doubts,name='doubts'),
    url(r'^alldoubts/$',views.alldoubts,name='alldoubts'),
    # url(r'^commenttry/$',views.commenttry,name='commenttry'),
    # url(r'^allcomments/$',views.allcomments,name='allcomments'),
    url(r'^postreply/([0-9]{2})/$',views.postreply,name='postreply')
]