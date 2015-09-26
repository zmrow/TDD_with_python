from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

  def setUp(self):
      self.browser = webdriver.Firefox()
      self.browser.implicitly_wait(3)

  def tearDown(self):
      self.browser.quit()

  def test_can_start_a_list_and_retrieve_it_later(self):
      # Go to the homepage to check out the app
      self.browser.get('http://localhost:8000')

      # The page title and header mention to-do lists
      self.assertIn('To-Do', self.browser.title)
      self.fail('Finish the test')

      # You can enter a to-do item

      # Type "Buy peacock feathers" in a text box

      # When you hit enter, the page updates and now the page lists
      # "1: Buy peacock feathers" as an item in a to-do list

      # There is still a text box inviting you to add another item.  Enter
      # "Use peacock feathers to make a fly"

      # Page updates again, and shows both items on the list

      # Will the site remember the list?  The site should generate a unique
      # url for you -- and there is some text to that effect

      # Visit that url, the list is still there

      # Go back to bed

if __name__ == '__main__':
    unittest.main(warnings='ignore')
