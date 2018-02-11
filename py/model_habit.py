""" The ndb Habit Model"""
from datetime import date
from model_task import Task
from google.appengine.ext import ndb
from google.appengine.api import users

class Habit(Task):
  """ndb Habit model

  Args:
    signup_days: the total days user have signed up
    strength: the habit strength in percentage
  """
  signup_days = ndb.BooleanProperty(repeated=True)
  strength = ndb.IntegerProperty()

  @classmethod
  def create(cls, title):
    """Create a new Habit.
       Set initial signup and strength to be zero.

    Args:
      title: the title of habit.

    Returns:
      Habit entity
    """
    habit = super(Habit, cls).create(title)
    habit.signup_days = 0
    habit.strength = 0
    habit.put()
    return habit

  @classmethod
  def sign_up(cls, id):
    """Sign up a hahit for a day.

    Args:
      id: the id of habit.
    """
    task = cls.get_task_by_id(int(id))
    task.signup_days += 1
    task.strength = cls._calculate_strength(task.signup_days,
                                            task.creation_date)

  @staticmethod
  def _calculate_strength(signup_days, create_date):
    """Calculate the strength of habit based on the sign up days.

    Args:
      signup_days: the number of days have signed up.
      create_date: the date when the habit is created.

    Returns:
      The strength of habit in percentage.
    """
    duration = (date.today() - create_date).days
