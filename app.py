import json
import webapp2
from model_habit import Habit

class RestHandler(webapp2.RequestHandler):
  def dispatch(self):
	super(RestHandler, self).dispatch()

  def SendJson(self, response):
	self.response.headers['content-type'] = 'text/plain'
	self.response.write(json.dumps(response))

class HabitSaveAndQuery(RestHandler):
  def post(self):
    response = json.loads(self.request.body)
    habit = Habit.create(response['title'])

  def get(self):
    habits = Habit.query_by_current_user()
    response = [habit.display_task() for habit in habits]
    self.SendJson(response)

APP = webapp2.WSGIApplication([
    ('/service/habit', HabitSaveAndQuery)
], debug=True)
