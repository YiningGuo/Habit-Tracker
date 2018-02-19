""" The ndb Habit Model"""
from datetime import date
from model_task import Task
from datetime import timedelta
from google.appengine.ext import ndb
from google.appengine.api import users

class Habit(Task):
  """ndb Habit model

  Args:
    total_days: the total days user have signed up
    max_streak: the max streak of signing up
    cache_start_day: the day to start a 22 days period
    cache_signups: a boolean list keeps track of each day's
                   sign up in a a 22 days period
    strength: the habit strength in percentage
  """
  total_days = ndb.IntegerProperty()
  max_streak = ndb.IntegerProperty()
  cache_start_day = ndb.DateProperty(auto_now_add=True)
  cache_signups = ndb.BooleanProperty(repeated=True)
  strength = ndb.ComputedProperty(
      lambda self: round(sum(self.cache_signups)/float(self.HABIT_STREAK), 2))

  # Assume it takes 22 days to caltivate a strong habit
  HABIT_STREAK = 22

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
    habit.total_days = 0
    habit.max_streak = 0
    habit.put()
    return habit

  @classmethod
  def sign_up(cls, id):
    """Sign up a hahit for a day.

    Args:
      id: the id of habit.
    """
    task = cls.get_task_by_id(int(id))
    duration = (date.today() - task.cache_start_day).days
    if duration > cls.HABIT_STREAK:
      absent_days = duration - cls.HABIT_STREAK
      task.cache_start_day += timedelta(days = absent_days)
      task._update_signup_days(absent_days)
    else:
      task._update_signup_days(0)
    task._update_max_streak()
    task.total_days += 1
    task.put()

  def _update_signup_days(self, absent_days):
    """Update signup days field.

    Args:
      absent_days: the number of days need to be recalculated
                   for current period.
    """
    if absent_days > 0:
      self.cache_signups = self.cache_signups[absent_days:]
      self.cache_signups += [False] * (
          self.HABIT_STREAK - 1 - len(self.cache_signups))
      self.cache_signups.append(True)
    else:
      self.cache_signups.append(True)

  def _update_max_streak(self):
    """Update the max_strak field. """
    curr_streak = 0
    for i in range(len(self.cache_signups) - 1, -1, -1):
      if self.cache_signups[i]:
        curr_streak += 1
      else:
        break;
    self.max_streak = max(curr_streak, self.max_streak)
