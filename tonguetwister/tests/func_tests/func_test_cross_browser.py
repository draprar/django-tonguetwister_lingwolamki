import os
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
import platform


class CrossBrowserTest(unittest.TestCase):

    def setUp(self):
        # Set base URL and initialize drivers for Chrome, Firefox, and Edge
        self.base_url = "https://tonguetwister.pythonanywhere.com/"
        self.browsers = {
            "chrome": webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())),
            "firefox": webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install())),
            "edge": webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install())),
        }

        # Add Safari driver for MacOS
        if platform.system() == "Darwin":
            self.browsers["safari"] = webdriver.Safari()

    def test_home_page_response(self):
        # Verify that each browser can open the homepage and check the page title
        for browser_name, driver in self.browsers.items():
            with self.subTest(browser=browser_name):
                driver.get(self.base_url)
                self.assertIn("TongueTwister", driver.title)
                driver.quit()

    def tearDown(self):
        # Quit all open browser drivers
        for driver in self.browsers.values():
            driver.quit()


if __name__ == "__main__":
    # Define output directory and file for test results
    test_dir = os.path.join(os.getcwd(), 'tests_outcomes')
    os.makedirs(test_dir, exist_ok=True)
    test_outcome_file = os.path.join(test_dir, 'test_cross_browser_outcome.txt')

    # Run tests and save results to a file
    with open(test_outcome_file, 'w') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        result = unittest.main(testRunner=runner, exit=False)

    print(f"Test results written to {test_outcome_file}")
