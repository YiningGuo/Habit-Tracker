import os
import sys
import unittest
from google.appengine.ext import testbed


class TestTool(unittest.TestCase):
  """Test set up tools for unit testing"""
  lib_path = os.path.abspath(os.path.join(__file__, '..', '..', 'py'))
  sys.path.append(lib_path)
  test_email = "test@example.com"
  user_id = '123'

  def set_test(self):
    os.environ['ENV'] = 'prod'
    self.testbed = testbed.Testbed()
    self.testbed.activate()
    self.testbed.setup_env(USER_EMAIL=self.test_email, USER_ID=self.user_id,
                           USER_IS_ADMIN='1', overwrite=True)
    self.testbed.init_user_stub()
    self.testbed.init_datastore_v3_stub()
    self.testbed.init_memcache_stub()

  def tearDown(self):
    self.testbed.deactivate()

  def set_user(self, email, id):
    self.test_email = email
    self.user_id = id
    self.testbed.setup_env(USER_EMAIL=email, USER_ID=id)

  def set_non_admin(self):
    self.testbed.setup_env(USER_IS_ADMIN='0')
