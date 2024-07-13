from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

url = "https://docs.google.com/forms/d/e/1FAIpQLSdUCd3UWQ3VOgeg0ZzNeT-xzNawU8AJ7Xidml-w1vhfBcvBWQ/viewform"
driver.get(url)

def fill_form(fullname, contact, email, address, pincode, dob, gender, code):
    try:
        inputs = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "whsOnd"))
        )

        additional_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".KHxj8b.tL9Q4c"))
        )
        
        inputs.append(additional_input)

        inputs = [WebDriverWait(driver, 20).until(EC.element_to_be_clickable(element)) for element in inputs]
        
        inputs_array = [fullname, contact, email, address, pincode, dob, gender, code]
        
        if len(inputs) != len(inputs_array):
            print("Number of input fields does not match the data provided.")
            return
        
        for i in range(len(inputs)):
            inputs[i].clear()
            inputs[i].send_keys(inputs_array[i])
        
    except Exception as e:
        print(f"An error occurred: {e}")

fill_form("Kartik Dubey", "8356974185", "kartiktornadus098@gmail.com", "400054", "05242003", "male", "GNFPYC", "MSEB colony, Santacruz West")

submit_button = driver.find_element(By.CLASS_NAME, "NPEfkd")
submit_button.click()

time.sleep(10)
driver.quit()
