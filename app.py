import json
import webapp2
from model_habit import Habit

class RestHandler(webapp2.RequestHandler):
  def dispatch(self):
	super(RestHandler, self).dispatch()

  def SendJson(self, response):
	self.response.headers['content-type'] = 'text/plain'
	self.response.write(json.dumps(response))

class HabitGetUpdateAndDelete(RestHandler):
  def post(self, id):
    response = json.loads(self.request.body)
    habit = Habit.create(response['title'])

  def get(self, id):
    response =     

APP = webapp2.WSGIApplication([
    ('/service/habit/(\d+)', HabitGetUpdateAndDelete)
], debug=True)
