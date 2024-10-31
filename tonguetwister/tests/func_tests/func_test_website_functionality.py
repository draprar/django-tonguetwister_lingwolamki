import os
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class NavbarLogoClickabilityTest(unittest.TestCase):

    def setUp(self):
        # Set up Chrome WebDriver
        self.driver = webdriver.Chrome()

    def test_toggler_is_clickable(self):
        # Verify navbar logo is clickable and toggles navbar content visibility
        self.driver.get("http://127.0.0.1:8000/")
        nav_toggler = self.driver.find_element(By.ID, "nav-logo")
        self.assertTrue(nav_toggler.is_enabled())
        nav_toggler.click()
        navbar_content = self.driver.find_element(By.ID, 'navbarToggleExternalContent')
        assert navbar_content.is_displayed()
        nav_toggler.click()

    def tearDown(self):
        # Quit WebDriver
        self.driver.quit()


class SliderTest(unittest.TestCase):

    def setUp(self):
        # Set up Chrome WebDriver
        self.driver = webdriver.Chrome()

    def test_swipe_slider(self):
        # Test swiping action on slider element
        self.driver.get("http://127.0.0.1:8000/")
        slider = self.driver.find_element(By.ID, "mySwiper")
        action = webdriver.ActionChains(self.driver)
        action.click_and_hold(slider).move_by_offset(50, 0).release().perform()

    def test_buttons_are_clickable(self):
        # Test that all visible and enabled buttons are clickable
        self.driver.get("http://127.0.0.1:8000/")
        buttons = self.driver.find_elements(By.TAG_NAME, "button")
        for button in buttons:
            if button.is_displayed() and button.is_enabled():
                button.click()

    def tearDown(self):
        # Quit WebDriver
        self.driver.quit()


class LoadMoreButtonsTest(unittest.TestCase):

    def setUp(self):
        # Set up Chrome WebDriver
        self.driver = webdriver.Chrome()

    def wait_for_element(self, by, value, timeout=10):
        # Wait for element to be located
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, value)))

    def test_load_more_articulators(self):
        # Test load more functionality for articulators
        self.driver.get("http://127.0.0.1:8000/")
        load_more_btn = self.driver.find_element(By.ID, "load-more-btn")
        while load_more_btn.is_displayed():
            load_more_btn.click()
            time.sleep(2)
            load_more_btn = self.driver.find_element(By.ID, "load-more-btn")
        self.assertFalse(load_more_btn.is_displayed())

    def test_load_more_exercises(self):
        # Test load more functionality for exercises
        self.driver.get("http://127.0.0.1:8000/")
        load_more_exercises_btn = self.driver.find_element(By.ID, "load-more-exercises-btn")
        while load_more_exercises_btn.is_displayed():
            load_more_exercises_btn.click()
            time.sleep(2)
            load_more_exercises_btn = self.driver.find_element(By.ID, "load-more-exercises-btn")
        self.assertFalse(load_more_exercises_btn.is_displayed())

    def test_load_more_twisters(self):
        # Test load more functionality for twisters
        self.driver.get("http://127.0.0.1:8000/")
        recalculate_height_btn = self.wait_for_element(By.ID, "recalculate-height", timeout=20)
        while recalculate_height_btn.is_displayed():
            recalculate_height_btn.click()
            time.sleep(2)
            recalculate_height_btn = self.wait_for_element(By.ID, "recalculate-height", timeout=2)
            self.assertFalse(recalculate_height_btn.is_displayed())

    def test_load_more_trivia(self):
        # Test load more functionality for trivia
        self.driver.get("http://127.0.0.1:8000/")
        load_more_trivia_btn = self.driver.find_element(By.ID, "load-more-trivia-btn")
        while load_more_trivia_btn.is_displayed():
            load_more_trivia_btn.click()
            time.sleep(2)
            load_more_trivia_btn = self.driver.find_element(By.ID, "load-more-trivia-btn")
        self.assertFalse(load_more_trivia_btn.is_displayed())

    def test_load_more_facts(self):
        # Test load more functionality for facts
        self.driver.get("http://127.0.0.1:8000/")
        load_more_facts_btn = self.driver.find_element(By.ID, "load-more-facts-btn")
        while load_more_facts_btn.is_displayed():
            load_more_facts_btn.click()
            time.sleep(2)
            load_more_facts_btn = self.driver.find_element(By.ID, "load-more-facts-btn")
        self.assertFalse(load_more_facts_btn.is_displayed())

    def tearDown(self):
        # Quit WebDriver
        self.driver.quit()


class Error404Test(unittest.TestCase):

    def setUp(self):
        # Set up Chrome WebDriver
        self.driver = webdriver.Chrome()

    def test_404_page(self):
        # Test display and content of custom 404 error page
        self.driver.get("http://127.0.0.1:8000/na/")

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.TAG_NAME, "h1"))
        )

        error_message = self.driver.find_element(By.TAG_NAME, "h1")
        self.assertEqual(error_message.text, "404")

        error_description = self.driver.find_element(By.TAG_NAME, "p")
        self.assertIn("Ups! Strona nie istnieje.", error_description.text)

        # Click back button on 404 page
        self.driver.find_element(By.CSS_SELECTOR, "a[type='submit']").click()


if __name__ == "__main__":
    test_dir = os.path.join(os.getcwd(), 'tests_outcomes')
    os.makedirs(test_dir, exist_ok=True)
    test_outcome_file = os.path.join(test_dir, 'test_website_functionality_outcome.txt')

    with open(test_outcome_file, 'w') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        result = unittest.main(testRunner=runner, exit=False)

    print(f"Test results written to {test_outcome_file}")
