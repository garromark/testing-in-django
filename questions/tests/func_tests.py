from django.test import LiveServerTestCase
from selenium import webdriver

class QuestionsTest(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_read_vote_and_ask_a_question(self):
		# Isabel opens her web browser and visits Torquemada
		self.browser.get(self.live_server_url + '/')

		# She knows it's Torquemada because she sees the name
		# in the heading
		heading = self.browser.find_element_by_css_selector("h1#trq-heading")
		self.assertEqual(heading.text, "Torquemada")

		# She browses through the existing questions
		question_1 = self.browser.find_element_by_css_selector("div#trq-question-1 h4")
		self.assertEqual(question_1.text, "How can my team get started with testing?")
		question_2 = self.browser.find_element_by_css_selector("div#trq-question-2 h4")
		self.assertEqual(question_1.text, "Does Selenium only work in Firefox?")
		
		# She sees a question that she'd like to have answered,
		# and votes it up
		
		# She sees a silly question and votes it down. No
		# time for that type of stuff in a Django talk
		
		# She then asks a question of her own.

		# TODO
		self.fail('finish this test')
