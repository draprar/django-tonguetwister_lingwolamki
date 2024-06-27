import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddModifyDeleteTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_add_modify_delete_articulator(self):
        self.driver.get("http://127.0.0.1:8000/")

        # Login
        self.driver.find_element(By.LINK_TEXT, "Logowanie").click()
        self.driver.find_element(By.NAME, "username").send_keys("prt")
        self.driver.find_element(By.NAME, "password").send_keys("1")
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Wyloguj"))
        )

        # Enter Articulator settings
        self.driver.find_element(By.CSS_SELECTOR, "button[aria-label='settings'").click()
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "a[type='articulator-list'"))
        )
        self.driver.find_element(By.CSS_SELECTOR, "a[type='articulator-list'").click()

        # Add Articulator
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, "add-articulator"))
        )
        self.driver.find_element(By.ID, "add-articulator").click()
        self.driver.find_element(By.CSS_SELECTOR, "textarea[name='text'").send_keys('This is a test text.')
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit'").click()

        # Modify Articulator
        self.driver.find_element(By.LINK_TEXT, "Edytuj").click()
        self.driver.find_element(By.CSS_SELECTOR, "textarea[name='text'").clear()
        self.driver.find_element(By.CSS_SELECTOR, "textarea[name='text'").send_keys('This is a changed test text.')
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit'").click()

        # Delete Articulator
        self.driver.find_element(By.LINK_TEXT, "Usuń").click()
        self.driver.find_element(By.CSS_SELECTOR, "a[type='cancel'").click()
        self.driver.find_element(By.LINK_TEXT, "Usuń").click()
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit'").click()
        self.driver.find_element(By.CSS_SELECTOR, "a[type='go-back'").click()

        # Logout
        self.driver.find_element(By.LINK_TEXT, "Wyloguj").click()

    def test_add_modify_delete_exercise(self):
        self.driver.get("http://127.0.0.1:8000/")

        # Login
        self.driver.find_element(By.LINK_TEXT, "Logowanie").click()
        self.driver.find_element(By.NAME, "username").send_keys("prt")
        self.driver.find_element(By.NAME, "password").send_keys("1")
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Wyloguj"))
        )

        # Enter Exercise settings
        self.driver.find_element(By.CSS_SELECTOR, "button[aria-label='settings'").click()
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "a[type='exercise-list'"))
        )
        self.driver.find_element(By.CSS_SELECTOR, "a[type='exercise-list'").click()

        # Add Exercise
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, "add-exercise"))
        )
        self.driver.find_element(By.ID, "add-exercise").click()
        self.driver.find_element(By.CSS_SELECTOR, "textarea[name='text'").send_keys('This is a test text.')
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit'").click()

        # Modify Exercise
        self.driver.find_element(By.LINK_TEXT, "Edytuj").click()
        self.driver.find_element(By.CSS_SELECTOR, "textarea[name='text'").clear()
        self.driver.find_element(By.CSS_SELECTOR, "textarea[name='text'").send_keys('This is a changed test text.')
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit'").click()

        # Delete Exercise
        self.driver.find_element(By.LINK_TEXT, "Usuń").click()
        self.driver.find_element(By.CSS_SELECTOR, "a[type='cancel'").click()
        self.driver.find_element(By.LINK_TEXT, "Usuń").click()
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit'").click()
        self.driver.find_element(By.CSS_SELECTOR, "a[type='go-back'").click()

        # Logout
        self.driver.find_element(By.LINK_TEXT, "Wyloguj").click()

    def test_add_modify_delete_twister(self):
        self.driver.get("http://127.0.0.1:8000/")

        # Login
        self.driver.find_element(By.LINK_TEXT, "Logowanie").click()
        self.driver.find_element(By.NAME, "username").send_keys("prt")
        self.driver.find_element(By.NAME, "password").send_keys("1")
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Wyloguj"))
        )

        # Enter Twister settings
        self.driver.find_element(By.CSS_SELECTOR, "button[aria-label='settings'").click()
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "a[type='twister-list'"))
        )
        self.driver.find_element(By.CSS_SELECTOR, "a[type='twister-list'").click()

        # Add Twister
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, "add-twister"))
        )
        self.driver.find_element(By.ID, "add-twister").click()
        self.driver.find_element(By.CSS_SELECTOR, "textarea[name='text'").send_keys('This is a test text.')
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit'").click()

        # Modify Twister
        self.driver.find_element(By.LINK_TEXT, "Edytuj").click()
        self.driver.find_element(By.CSS_SELECTOR, "textarea[name='text'").clear()
        self.driver.find_element(By.CSS_SELECTOR, "textarea[name='text'").send_keys('This is a changed test text.')
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit'").click()

        # Delete Twister
        self.driver.find_element(By.LINK_TEXT, "Usuń").click()
        self.driver.find_element(By.CSS_SELECTOR, "a[type='cancel'").click()
        self.driver.find_element(By.LINK_TEXT, "Usuń").click()
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit'").click()
        self.driver.find_element(By.CSS_SELECTOR, "a[type='go-back'").click()

        # Logout
        self.driver.find_element(By.LINK_TEXT, "Wyloguj").click()

    def test_add_modify_delete_trivia(self):
        self.driver.get("http://127.0.0.1:8000/")

        # Login
        self.driver.find_element(By.LINK_TEXT, "Logowanie").click()
        self.driver.find_element(By.NAME, "username").send_keys("prt")
        self.driver.find_element(By.NAME, "password").send_keys("1")
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Wyloguj"))
        )

        # Enter Trivia settings
        self.driver.find_element(By.CSS_SELECTOR, "button[aria-label='settings'").click()
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "a[type='trivia-list'"))
        )
        self.driver.find_element(By.CSS_SELECTOR, "a[type='trivia-list'").click()

        # Add Trivia
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, "add-trivia"))
        )
        self.driver.find_element(By.ID, "add-trivia").click()
        self.driver.find_element(By.CSS_SELECTOR, "textarea[name='text'").send_keys('This is a test text.')
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit'").click()

        # Modify Trivia
        self.driver.find_element(By.LINK_TEXT, "Edytuj").click()
        self.driver.find_element(By.CSS_SELECTOR, "textarea[name='text'").clear()
        self.driver.find_element(By.CSS_SELECTOR, "textarea[name='text'").send_keys('This is a changed test text.')
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit'").click()

        # Delete Trivia
        self.driver.find_element(By.LINK_TEXT, "Usuń").click()
        self.driver.find_element(By.CSS_SELECTOR, "a[type='cancel'").click()
        self.driver.find_element(By.LINK_TEXT, "Usuń").click()
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit'").click()
        self.driver.find_element(By.CSS_SELECTOR, "a[type='go-back'").click()

        # Logout
        self.driver.find_element(By.LINK_TEXT, "Wyloguj").click()

    def test_add_modify_delete_funfact(self):
        self.driver.get("http://127.0.0.1:8000/")

        # Login
        self.driver.find_element(By.LINK_TEXT, "Logowanie").click()
        self.driver.find_element(By.NAME, "username").send_keys("prt")
        self.driver.find_element(By.NAME, "password").send_keys("1")
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Wyloguj"))
        )

        # Enter Funfact settings
        self.driver.find_element(By.CSS_SELECTOR, "button[aria-label='settings'").click()
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "a[type='funfact-list'"))
        )
        self.driver.find_element(By.CSS_SELECTOR, "a[type='funfact-list'").click()

        # Add Funfact
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, "add-funfact"))
        )
        self.driver.find_element(By.ID, "add-funfact").click()
        self.driver.find_element(By.CSS_SELECTOR, "textarea[name='text'").send_keys('This is a test text.')
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit'").click()

        # Modify Funfact
        self.driver.find_element(By.LINK_TEXT, "Edytuj").click()
        self.driver.find_element(By.CSS_SELECTOR, "textarea[name='text'").clear()
        self.driver.find_element(By.CSS_SELECTOR, "textarea[name='text'").send_keys('This is a changed test text.')
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit'").click()

        # Delete Funfact
        self.driver.find_element(By.LINK_TEXT, "Usuń").click()
        self.driver.find_element(By.CSS_SELECTOR, "a[type='cancel'").click()
        self.driver.find_element(By.LINK_TEXT, "Usuń").click()
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit'").click()
        self.driver.find_element(By.CSS_SELECTOR, "a[type='go-back'").click()

        # Logout
        self.driver.find_element(By.LINK_TEXT, "Wyloguj").click()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    test_dir = os.path.join(os.getcwd(), 'tests_outcomes')
    os.makedirs(test_dir, exist_ok=True)
    test_outcome_file = os.path.join(test_dir, 'test_add_modify_delete_outcome.txt')

    with open(test_outcome_file, 'w') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        result = unittest.main(testRunner=runner, exit=False)

    print(f"Test results written to {test_outcome_file}")