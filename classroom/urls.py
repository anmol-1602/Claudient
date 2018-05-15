from django.conf.urls import url

from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name='classroom'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^newdoubt/$',views.newdoubt,name='newdoubt'),
    url(r'^alldoubts/$',views.alldoubts,name='alldoubts'),
    url(r'^allassignments/$',views.allassignments,name='allassignments'),
    url(r'^addassignment/$',views.addassignment,name='addassignment'),
    url(r'^allnotices/$',views.allnotices,name='allnotices'),
    url(r'^moreuserinfo/$',views.moreuserinfo,name='moreuserinfo'),
    # url(r'^signup/$',views.signup,name='signup'),
    # url(r'^commenttry/$',views.commenttry,name='commenttry'),
    # url(r'^allcomments/$',views.allcomments,name='allcomments'),
   
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
