import unittest
import sys
import os

APP_ENGINE_PATH = '/Users/yiningguo/google-cloud-sdk/platform/google_appengine'
sys.path.insert(1, APP_ENGINE_PATH)
sys.path.insert(1, APP_ENGINE_PATH+'/lib/yaml/lib')

if 'google' in sys.modules:
    del sys.modules['google']

loader = unittest.TestLoader()
start_dir = 'tests/'
suite = loader.discover(start_dir)

runner = unittest.TextTestRunner()
runner.run(suite)
