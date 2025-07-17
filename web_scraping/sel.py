from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# options.add_argument("--enable-javascript")


def scrap_curp(curp):
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.gob.mx/curp/')

    curp_element = driver.find_element(By.ID, "curpinput")
    # curp.send_keys("GOPD960817HCCMCV05")
    curp_element.send_keys(curp)

    wait = WebDriverWait(driver, 5)

    wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))

    captcha = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']")))
    captcha.click()

    sleep(10)

    driver.switch_to.default_content()

    button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[id='searchButton']")))
    button.submit()

    # sleep(5)

    data = {}
    # data_process = {}

    not_passed = {}

    try:
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".panel.panel-default")))

        tr = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "tr > td")))

        texts = [td.text for td in tr]

        data = {texts[i]: texts[i + 1] for i in range(0, len(texts), 2)}

        # for clave, valor in data.items():
        #     if clave in data_process:
        #         data_process[clave] = data_process[clave].append(valor)
        #     else:
        #         data_process.update({clave: [valor]})

    except Exception:
        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal-content")))
            not_passed = {'curp': curp, 'observacion' : 'No es válido ante el RENAPO'}
        except Exception:
            not_passed = {'curp': curp, 'observacion' : 'No paso el captcha'}

    # sleep(2)

    driver.close()

    return data, not_passed