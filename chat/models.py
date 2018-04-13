from django.db import models
from django.utils.six import python_2_unicode_compatible
import json
from .settings import MSG_TYPE_MESSAGE
# Create your models here.


@python_2_unicode_compatible
class Room(models.Model):

	title=models.CharField(max_length=255)
	staff_only=models.BooleanField(default=False)

	def str(self):
		return self.title

	@property
	def websocket_group(self):
		return Group("room-%s" % self.id)


	def send_message(self,message,user,msg_type=MSG_TYPE_MESSAGE):
		final_msg={'room':str(self.id),'message':message,'ussername':user.username,'msg_type':msg_type}

		self.websocket_group.s
		end(
			{"text":json.dumps(final_msg)}
		)