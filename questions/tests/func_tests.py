from django.test import LiveServerTestCase
from selenium import webdriver

import time

class QuestionsTest(LiveServerTestCase):
	
	fixtures = ['questions',]

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
		self.assertEqual(question_2.text, "Does Selenium only work in Firefox?")
				
		# She sees a question that she'd like to have answered, and votes it up
		vote_for_2 = self.browser.find_element_by_css_selector("div#trq-question-2 a.trq-vote-up").click()
		vote_tally = self.browser.find_element_by_css_selector("div#trq-question-2 .trq-vote-count")
		self.assertEqual(vote_tally.text, "Votes: 1")
		
		# Her voted up question is now at the top of the list
		all_questions = self.browser.find_elements_by_css_selector("div.trq-question")
		self.assertEqual(all_questions[0].get_attribute("id"), "trq-question-2")
		
		# She sees a silly question and votes it down. No time for that type of stuff 
		# in a Django talk
		question_3 = self.browser.find_element_by_css_selector("div#trq-question-3 h4")
		self.assertEqual(question_3.text, "Why didn't you build this in Wordpress?")
		vote_down_3 = self.browser.find_element_by_css_selector("div#trq-question-3 a.trq-vote-down").click()
		vote_tally_3 = self.browser.find_element_by_css_selector("div#trq-question-3 .trq-vote-count")
		self.assertEqual(vote_tally_3.text, "Votes: -1")
		
		# She then asks a question of her own.
		text_field = self.browser.find_element_by_css_selector("input#id_text")
		text_field.clear()
		text_field.send_keys("Why aren't using reverse() for your URLs in views?")
		self.browser.find_element_by_css_selector("input#trq-submit-question").click()
		
		self.assertContains(self.browser.find_element_by_css_selector("div#trq-question-4 h4"),
							"Why aren't using reverse() for your URLs in views?")
