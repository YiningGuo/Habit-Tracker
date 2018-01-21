from tools import TestTool
from py import model_task as model


class TaskTestCase(TestTool):
  def setUp(self):
    self.set_test()

  def test_create(self):
    task = model.Task.create('test')
    self._assert_tasks(1, ['test'])

  def _assert_tasks(self, test_num, test_titles):
    tasks = model.Task.query_by_current_user()
    self.assertEqual(test_num, tasks.count())
    for i, task in enumerate(tasks):
      self._assert_task(task, test_titles[i])

  def _assert_task(self, task, title):
    task = task.display_task()
    self.assertEqual(task['title'], title)
