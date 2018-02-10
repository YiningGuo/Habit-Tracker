""" The ndb Habit Model"""
from model_task import Task
from google.appengine.ext import ndb
from google.appengine.api import users

class Habit(Task):
  """ndb Habit model

  Args:
    signup_days: the total days user have signed up
    strength: the habit strength in percentage
  """
  signup_days = ndb.IntegerProperty()
  strength = ndb.IntegerProperty()

  @classmethod
  def create(cls, title):
    habit = super(Habit, cls).create(title)
    habit.signup_days = 0
    habit.strength = 0
    habit.put()
    return habit
