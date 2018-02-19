from datetime import date
from tools import TestTool
from datetime import timedelta
from py.model_habit import Habit

class TaskTestCase(TestTool):
  def setUp(self):
    self.set_test()
    self.habit = Habit.create('test')
    self.habit_id = self.habit.key.id()

  def test_create(self):
    self._assert_initial(self.habit, 'test')

  def test_query(self):
    habit = Habit.query().fetch().pop()
    self.assertEqual(habit._get_kind(), 'Habit')
    self._assert_initial(habit, 'test')

  def test_update(self):
    habit = Habit.update(self.habit_id, 'change')
    self._assert_initial(habit, 'change')

  def test_delete(self):
    Habit.delete(self.habit_id)
    habits = Habit.query().fetch()
    self.assertEqual(0, len(habits))

  def test_signup(self):
    Habit.sign_up(self.habit_id)
    self.assertEqual(0.05, self.habit.strength)
    self.assertEqual(1, self.habit.total_days)
    self.assertEqual(1, self.habit.max_streak)

  def test_exceed_period_signup(self):
    fake_record = [True] * 21
    fake_create_date = date.today() - timedelta(days = 30)
    self.habit.cache_signups = fake_record
    self.habit.cache_start_day = fake_create_date
    self.habit.put()
    Habit.sign_up(self.habit_id)
    self.assertEqual(0.64, self.habit.strength)

  def _assert_initial(self, habit, title):
    self.assertEqual(title, self.habit.title)
    self.assertEqual([], self.habit.cache_signups)
    self.assertEqual(0, self.habit.strength)
    self.assertEqual(0, self.habit.total_days)
    self.assertEqual(0, self.habit.max_streak)
