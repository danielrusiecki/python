from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.common.action_chains import ActionChains
# from time import sleep

daniel_id = ""   # TYPE LOGIN NUMBER HERE !
daniel_pwd = ""  # TYPE PASSWORD HERE !


def click_zaloguj():
    WebDriverWait(driver, 5).until(ec.visibility_of_element_located(
        (By.XPATH, '//input[@value="Zaloguj"]'))).click()


def type_credentials(username, password):
    WebDriverWait(driver, 5).until(ec.visibility_of_element_located(
        (By.XPATH, '//input[@id="UserName"]'))).send_keys(username)
    WebDriverWait(driver, 5).until(ec.visibility_of_element_located(
        (By.XPATH, '//input[@id="Password"]'))).send_keys(password + Keys.ENTER)


def click_zamknij_button():
    try:
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located(
            (By.XPATH, '//button[contains(text(),"Zamknij")]'))).click()
    except TimeoutException as es:
        print("Something went wrong, here is an exception message (if exists): " + es.msg)


def click_medicover_home():
    WebDriverWait(driver, 5).until(ec.visibility_of_element_located(
        (By.XPATH, '//img[@alt="Medicover"]'))).click()


def click_umow_wizyte():
    WebDriverWait(driver, 8).until(ec.visibility_of_element_located(
        (By.XPATH, '//div[@id="tripel-singlebox"]//a[contains(text(),"Umów wizytę")]'))).click()


def select_nie_buttons():
    WebDriverWait(driver, 8).until(ec.visibility_of_element_located(
        (By.XPATH, '//span[text()="Nie"]')))
    spannie = driver.find_elements_by_xpath('//span[text()="Nie"]')
    spannie[0].click()
    spannie[1].click()
    spannie[2].click()


def click_dalej():
    driver.find_element_by_xpath('//a[contains(text(),"Dalej")]').click()


def click_wizyta_w_centrum():
    WebDriverWait(driver, 3).until(ec.visibility_of_element_located(
        (By.XPATH, '//a[text()="Wizyta w Centrum"]'))).click()


# ========================= CODE ==========================
driver = webdriver.Chrome()
driver.get("https://mol.medicover.pl/Users/Account/AccessDenied?ReturnUrl=%2F")
window_before = driver.window_handles[0]
click_zaloguj()
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
type_credentials(daniel_id, daniel_pwd)
driver.switch_to.window(window_before)

click_zamknij_button()
click_medicover_home()
click_zamknij_button()
click_umow_wizyte()

WebDriverWait(driver, 8).until(ec.visibility_of_element_located(
        (By.XPATH, '//a[@role="button" and contains(text(),"Internista")]'))).click()

elem2 = driver.find_element_by_xpath('//*[@id="simplecases-coldandflu-bookappointment-modal"]/a')
# rozwiazanie na przypadek gdy element is interactable:
driver.execute_script("arguments[0].click();", elem2)

select_nie_buttons()
click_dalej()
click_wizyta_w_centrum()
