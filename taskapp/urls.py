from django.conf.urls import url,include


from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name='taskapp'


urlpatterns = [
	url(r'^accounts/', include('allauth.urls')),
    url(r'^$', views.home, name='home'),
    url(r'^tasks/$',views.tasks,name='tasks'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^addtask/$',views.addtask,name='addtask'),
    url(r'^complete/(?P<taskid>\d+)/$',views.complete,name='complete'),
    url(r'^incomplete/(?P<taskid>\d+)/$',views.incomplete,name='incomplete'),
    url(r'^edittask/(?P<taskid>\d+)/$',views.edittask,name='edittask'),
    url(r'^moveup/(?P<prid>\d+)/$',views.moveup,name='moveup'),
    url(r'^movedown/(?P<prid>\d+)/$',views.movedown,name='movedown')
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)