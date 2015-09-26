from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
      header_text = self.browser.find_element_by_tag_name('h1').text
      self.assertIn('To-Do', header_text)

      # You can enter a to-do item
      inputbox = self.browser.find_element_by_id('id_new_item')
      self.assertEqual(
          inputbox.get_attribute('placeholder'),
          'Enter a to-do item'
      )

      # Type "Buy peacock feathers" in a text box
      inputbox.send_keys('Buy peacock feathers')

      # When you hit enter, the page updates and now the page lists
      # "1: Buy peacock feathers" as an item in a to-do list
      inputbox.send_keys(Keys.ENTER)

      table = self.browser.find_element_by_id('id_list_table')
      rows = table.find_elements_by_tag_name('tr')
      self.assertTrue(
          any(row.text == '1: Buy peacock feathers' for row in rows)
      )

      # There is still a text box inviting you to add another item.  Enter
      # "Use peacock feathers to make a fly"
      self.fail('Finish the test')

      # Page updates again, and shows both items on the list

      # Will the site remember the list?  The site should generate a unique
      # url for you -- and there is some text to that effect

      # Visit that url, the list is still there

      # Go back to bed

if __name__ == '__main__':
    unittest.main(warnings='ignore')
