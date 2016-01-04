from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.template.context_processors import csrf

from lists.views import home_page

# Create your tests here.
class HomePageTest(TestCase):
	def test_root_url_resolve(self):
		found = resolve('/')
		self.assertEqual(found.func,home_page)

	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		c = {}
		c.update(csrf(request))
		expected_html = render_to_string('home.html',c)
		self.assertEqual(response.content.decode(),expected_html)

	def test_home_page_can_save_a_POST_request(self):
		request = HttpRequest()
		request.method = 'POST'
		request.POST['item_text'] = 'A new list item'
		response = home_page(request)
		self.assertIn('A new list item',response.content.decode())
		c = {}
		c.update(csrf(request))
		c['new_item_text']='A new list item'
		expected_html = render_to_string(
			'home.html',c
			)
		self.assertEqual(response.content.decode(),expected_html)