import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class PageResponseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_page_response(self):
        self.driver.get("http://127.0.0.1:8000/")
        self.assertIn("TongueTwister", self.driver.title)

    def tearDown(self):
        self.driver.quit()


class ElementClickabilityTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_element_clickable(self):
        self.driver.get("http://127.0.0.1:8000/")
        button = self.driver.find_element(By.ID, "nav-logo")
        self.assertTrue(button.is_enabled())
        button.click()

    def tearDown(self):
        self.driver.quit()


class SliderTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_swipe_slider(self):
        self.driver.get("http://127.0.0.1:8000/")
        slider = self.driver.find_element(By.ID, "mySwiper")
        action = webdriver.ActionChains(self.driver)
        action.click_and_hold(slider).move_by_offset(50, 0).release().perform()

    def tearDown(self):
        self.driver.quit()


class ClickAllButtonsTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_click_all_buttons(self):
        self.driver.get("http://127.0.0.1:8000/")
        buttons = self.driver.find_elements(By.TAG_NAME, "button")
        for button in buttons:
            if button.is_displayed() and button.is_enabled():
                button.click()

    def tearDown(self):
        self.driver.quit()


