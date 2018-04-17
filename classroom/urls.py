from django.conf.urls import url

from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name='classroom'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/$',views.signup,name='signup'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^doubts/$',views.doubts,name='doubts'),
    url(r'^alldoubts/$',views.alldoubts,name='alldoubts'),
    url(r'^allassignments/$',views.allassignments,name='allassignments'),
    url(r'^addassignment/$',views.addassignment,name='addassignment'),

    # url(r'^commenttry/$',views.commenttry,name='commenttry'),
    # url(r'^allcomments/$',views.allcomments,name='allcomments'),
    url(r'^postreply/([0-9]{2})/$',views.postreply,name='postreply')
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
