from tools import TestTool
from py.model_habit import Habit

class TaskTestCase(TestTool):
  def setUp(self):
    self.set_test()
    self.habit = Habit.create('test')
    self.habit_id = self.habit.key.id()

  def test_create(self):
    self.assertEqual('test', self.habit.title)
    self.assertEqual(0, self.habit.signup_days)
    self.assertEqual(0, self.habit.strength)
