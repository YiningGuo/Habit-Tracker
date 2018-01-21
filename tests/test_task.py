from tools import TestTool
from py import model_task as model


class TaskTestCase(TestTool):
  def setUp(self):
    self.set_test()
    self.task = model.Task.create('test')
    self.task_id = self.task.key.id()

  def test_create(self):
    self._assert_tasks(1, ['test'])

  def test_create_more(self):
    model.Task.create('test2')
    self._assert_tasks(2, ['test', 'test2'])

  def test_update(self):
    model.Task.update(self.task_id, 'test2')
    self._assert_tasks(1, ['test2'])

  def test_delete(self):
    model.Task.delete(self.task_id)
    self._assert_tasks(0, [])

  def test_create_empty(self):
    with self.assertRaises(model.TaskUpdateError) as msg:
      model.Task.create('')
    self.assertTrue('Invalid title.' in msg.exception)

  def test_create_whitespaces(self):
    with self.assertRaises(model.TaskUpdateError) as msg:
      model.Task.create('  \n')
    self.assertTrue('Invalid title.' in msg.exception)

  def test_update_empty(self):
    with self.assertRaises(model.TaskUpdateError) as msg:
      model.Task.update(self.task_id, ' ')
    self.assertTrue('Invalid title.' in msg.exception)

  def test_update_invalid_id(self):
    with self.assertRaises(model.TaskUpdateError) as msg:
      model.Task.update('123', 'test2')
    self.assertTrue('Invalid task id.' in msg.exception)

  def test_delete_invalid_id(self):
    with self.assertRaises(model.TaskUpdateError) as msg:
      model.Task.delete('123')
    self.assertTrue('Invalid task id.' in msg.exception)

  def _assert_tasks(self, test_num, test_titles):
    tasks = model.Task.query_by_current_user()
    self.assertEqual(test_num, tasks.count())
    for i, task in enumerate(tasks):
      self._assert_task(task, test_titles[i])

  def _assert_task(self, task, title):
    task = task.display_task()
    self.assertEqual(task['title'], title)
    self.assertEqual(task['owner'], self.test_email)
    self.assertTrue(task['create'])
