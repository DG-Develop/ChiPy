from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

# options = webdriver.ChromeOptions()
# options.add_argument("--enable-javascript")

# driver = webdriver.Chrome()

# driver.get('https://www.gob.mx/curp/')

# # assert "Python" in driver.title

# elem = driver.find_element(By.ID, "ember313")

# # elem.clear()
# # elem.send_keys("pycon")
# # elem.send_keys(Keys.RETURN)

# # assert "No results found." not in driver.page_source

# driver.close()

options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)
driver.get('https://www.gob.mx/curp/')

curp = driver.find_element(By.ID, "curpinput")
curp.send_keys("GOPD860817HCCMCV05")

WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()

search_button = driver.find_element(By.ID, "searchButton")
