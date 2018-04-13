import json

class CLientError(Exception):
	def init(self,code):
		super(CLientError,self).init(code)
		self.code=code

	def send_to(self,channel):
		channel.send({
			"text":json.dumps({
				"error":self.code,
			}),
		})