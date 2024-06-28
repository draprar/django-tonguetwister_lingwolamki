import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddDeleteUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.admin_url = "http://127.0.0.1:8000/admin/"
        self.username = "prt"
        self.password = "1"

    def test_login(self):
        self.driver.get(self.admin_url)

        self.driver.find_element(By.NAME, "username").send_keys(self.username)
        self.driver.find_element(By.NAME, "password").send_keys(self.password)
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, "site-name"))
        )
        self.assertIn("Administracja stroną", self.driver.title)

    def test_add_user(self):
        self.test_login()

        self.driver.find_element(By.LINK_TEXT, "Użytkownicy").click()
        self.driver.find_element(By.LINK_TEXT, "DODAJ UŻYTKOWNIK").click()

        self.driver.find_element(By.NAME, "username").send_keys("testuser")
        self.driver.find_element(By.NAME, "password1").send_keys("password123A(*7g&")
        self.driver.find_element(By.NAME, "password2").send_keys("password123A(*7g&")
        self.driver.find_element(By.NAME, "_save").click()

        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "testuser"))
        )
        self.assertTrue(self.driver.find_element(By.LINK_TEXT, "testuser"))

    def test_delete_user(self):
        self.test_login()

        self.driver.find_element(By.LINK_TEXT, "Użytkownicy").click()
        self.driver.find_element(By.LINK_TEXT, "testuser").click()

        self.driver.find_element(By.LINK_TEXT, "Usuń").click()
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit'").click()

        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "testuser"))
        )
        self.assertTrue(self.driver.find_element(By.LINK_TEXT, "testuser"))

    def test_logout(self):
        self.test_login()

        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        self.driver.get(self.admin_url)

        self.assertIn("Zaloguj się", self.driver.title)

    def tearDown(self):
        self.driver.quit()


class AddDeleteGroup(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.admin_url = "http://127.0.0.1:8000/admin/"
        self.username = "prt"
        self.password = "1"

    def test_login(self):
        self.driver.get(self.admin_url)

        self.driver.find_element(By.NAME, "username").send_keys(self.username)
        self.driver.find_element(By.NAME, "password").send_keys(self.password)
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, "site-name"))
        )
        self.assertIn("Administracja stroną", self.driver.title)

    def test_add_group(self):
        self.test_login()

        self.driver.find_element(By.LINK_TEXT, "Grupy").click()
        self.driver.find_element(By.LINK_TEXT, "DODAJ GRUPA").click()

        self.driver.find_element(By.ID, "id_name").send_keys("testgroup")
        self.driver.find_element(By.NAME, "_save").click()

        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "testgroup"))
        )
        self.assertTrue(self.driver.find_element(By.LINK_TEXT, "testgroup"))

    def test_delete_group(self):
        self.test_login()

        self.driver.find_element(By.LINK_TEXT, "Grupy").click()
        self.driver.find_element(By.LINK_TEXT, "testgroup").click()

        self.driver.find_element(By.LINK_TEXT, "Usuń").click()
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit'").click()

        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "testgroup"))
        )
        self.assertTrue(self.driver.find_element(By.LINK_TEXT, "testgroup"))

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    test_dir = os.path.join(os.getcwd(), 'tests_outcomes')
    os.makedirs(test_dir, exist_ok=True)
    test_outcome_file = os.path.join(test_dir, 'test_admin_outcome.txt')

    with open(test_outcome_file, 'w') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        result = unittest.main(testRunner=runner, exit=False)

    print(f"Test results written to {test_outcome_file}")
