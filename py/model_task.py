""" The ndb Task Model"""
from google.appengine.ext import ndb
from google.appengine.api import users


class TaskUpdateError(Exception):
  """Fired when attempting to update invalid Task."""
  pass


class Task(ndb.Model):
  """ndb Task model

  Properties:
    title: a one line description of a task.
    owner_id: the id of owner of the task.
    creation_time: the creation time of the task.
  """
  title = ndb.StringProperty()
  owner_id = ndb.StringProperty()
  creation_date = ndb.DateProperty(auto_now_add=True)

  @classmethod
  def query_by_current_user(cls):
    """Query tasks under current user."""
    current_user_id = users.get_current_user().user_id()
    return cls.query(Task.owner_id == current_user_id)

  @classmethod
  def create(cls, title):
    """Create a new Task.

    Args:
      title: the title of task.
    """
    title = cls._validate_title(title)
    owner_id = users.get_current_user().user_id()
    task = Task(title=title,
                owner_id=owner_id)
    task.put()
    return task

  @classmethod
  def update(cls, id, title):
    """Update the title of task with requested id.

    Args:
      id: the id of task.
      title: the new title.

    Raises:
      TaskUpdateError: when the task id is not valid.
    """
    title = cls._validate_title(title)
    task = Task.get_by_id(int(id))
    if not task:
      raise TaskUpdateError('Invalid task id.')
    task.title = title
    task.put()
    return task

  @classmethod
  def delete(cls, id):
    """Delete a task with requested id.

    Args:
      id: the id of task.
    """
    task = Task.get_by_id(int(id))
    task.delete()

  @classmethod
  def _validate_title(cls, title):
    """Validate the title

    Args:
      title: the input title.

    Raises:
      TaskUpdateError: when the title is empty.
    """
    title = title.strip()
    if not title:
      raise TaskUpdateError('Invalid title.')
    return title

  def display_task(self):
    """Convert Task to JSON format."""
    owner = users.User(_user_id=self.owner_id).email()
    create = self.creation_date.strftime('%d %b %Y')
    return {'id': self.key.id(), 'title': self.title,
			'owner': owner, 'create': create}
