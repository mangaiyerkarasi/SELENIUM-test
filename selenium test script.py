from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def test_google_search():
    """Open google.com, search for Selenium, and verify the results page."""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    with webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) as driver:
        driver.get("https://www.google.com")

        wait = WebDriverWait(driver, 10)

        # Accept any consent dialog if it appears
        try:
            consent_button = wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//button[normalize-space()='I agree' or normalize-space()='Accept all' or normalize-space()='Accept']",
                    )
                )
            )
            consent_button.click()
        except Exception:
            pass

        search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
        search_box.clear()
        search_box.send_keys("Selenium")
        search_box.send_keys(Keys.RETURN)

        wait.until(EC.title_contains("Selenium"))

        assert "Selenium" in driver.title


if __name__ == "__main__":
    test_google_search()
    print("Google search test completed successfully.")
