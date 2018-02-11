from tools import TestTool
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

  def _assert_initial(self, habit, title):
    self.assertEqual(title, self.habit.title)
    self.assertEqual(0, self.habit.signup_days)
    self.assertEqual(0, self.habit.strength)
