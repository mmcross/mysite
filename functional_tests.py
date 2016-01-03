from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Chrome()

	def tearDown(self):
		self.browser.close()

	def test_can_start(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('To-Do',self.browser.title)
		self.fail('finish')

if __name__ == '__main__':
	unittest.main(warnings='ignore')