from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start a new instance of Chrome webdriver
driver = webdriver.Chrome()

try:
    # Open the URL
    driver.get("https://www.instagram.com/guviofficial/")

    # Wait for the login popup to appear and close it if present
    try:
        login_popup = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'RnEpo')]"))
        )
        close_button = driver.find_element(By.XPATH, "//button[contains(@class, 'wpO6b')]")
        close_button.click()
    except:
        pass  # If the popup does not appear, continue

    # Wait for the followers element to be present
    followers_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(@href,'/guviofficial/followers/')]//span"))
    )
    # Extract the followers count
    followers_count = followers_element.get_attribute("title")

    # Wait for the following element to be present
    following_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(@href,'/guviofficial/following/')]//span"))
    )
    # Extract the following count
    following_count = following_element.text

    # Printing the results
    print("Total followers:", followers_count)
    print("Total following:", following_count)

except Exception as e:
    print("An error occurred:", e)

finally:
    # Close the browser
    driver.quit()
