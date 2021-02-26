import os
from time import sleep
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

var1 = "klawiatura"
# print('Wprowadz pierwszy szukany element:')
# var1 = input()
var2 = 'myszka'
# print("Wprowadz DRUGI szukany element:")
# var2 = input()


class AllegroSortBy(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_elem1_in_allegro(self):
        driver = self.driver
        # driver.implicitly_wait(5)

        driver.get("https://allegro.pl/")
        # driver.maximize_window()
        # sleep(4)

        # testowa asercja tytulu
        self.assertIn("najlepsze", driver.title)

        # *** 2 ***
        try:
            WebDriverWait(driver, 5).until(ec.visibility_of_element_located(
                (By.XPATH, '//button[contains(text(),"przejdź dalej")]'))).click()
        except TimeoutException as es:
            print("Something went wrong, here is an exception message (if exists): " + es.msg)

        elems3 = driver.find_elements_by_partial_link_text('WSZYSTKIE KAT')     # wielkosc liter ma znaczenie
        print(elems3)
        elems3[0].click()

        # wszystko w jednym, choc mozna tez uzyc z elem.submit()
        driver.find_element_by_xpath('//input[@type="search"]').send_keys(var1 + Keys.ENTER)

        # wybor Popularnosc: najwieksza
        popular = Select(driver.find_element_by_xpath('//select[@data-value="m"]'))
        popular.select_by_value('qd')

        # LUB PO TEKSCIE (ale tu chyba trzeba wczesniej dodac rozwijanie listy, jako ze jest 'visible_text'):
        # popular.select_by_visible_text(' popularność: największa ')
        assert "No results found." not in driver.page_source
        print("PIERWSZY PASSED!")

    def test_search_elem2_in_allegro(self):
        driver = self.driver
        driver.get("https://allegro.pl/")
        # driver.get("https://allegro.pl/")

        # czasami wywala bo za szybko sprawdza, zanim sie pojawi element, wiec lepsze z Try i ustawianiem czasu
        # ponadto wielkosc liter ma znaczenie
        # to faktycznie czasami sie wywala, trzeba dodac Implicit Wait
        # ale to dlatego ze to szczgolny przypadek bo to okno PRZEJDZ DALEJ pojawia sie po jakims czasie dopiero
        # tak normalnie dla innych elementow ktore maja byc lub nie to zadziala normalnie, chyba ze czekamy na nie
        if driver.find_elements_by_xpath("//button[contains(text(),'przejdź dalej')]"):
            driver.find_elements_by_xpath("//button[contains(text(),'przejdź dalej')]")[0].click()
        else:
            print('NIE MA TAKIEGO ELEMENTU')

        driver.find_element_by_partial_link_text('WSZYSTKIE KAT').click()

        # wszystko w jednym, choc mozna tez uzyc z elem.submit()
        driver.find_element_by_xpath('//input[@type="search"]').send_keys(var2 + Keys.ENTER)

        # wybor Czas do konca: najmniej
        Select(driver.find_element_by_xpath('//select[@data-value="m"]')).select_by_value('t')
        print('DRUGI PASSED!')

    def tearDown(self):
        # close the browser window (close zamyka aktualnie uzywane okno a quit zamyka wszystkie okna, chyba lepszy quit)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

# ------------------------------------------------------------------

# class PythonOrgSearch(unittest.TestCase):
#
#     def setUp(self):
#         self.driver = webdriver.Firefox()
#
#     def test_search_in_python_org(self):
#         driver = self.driver
#         driver.get("http://www.python.org")
#         self.assertIn("Python", driver.title)
#         elem = driver.find_element_by_name("q")
#         elem.send_keys("pycon")
#         elem.send_keys(Keys.RETURN)
#         assert "No results found." not in driver.page_source
#
#     def tearDown(self):
#         self.driver.close()
#
# if __name__ == "__main__":
#     unittest.main()

# ---------------------------------------

# from selenium import webdriver
# b = webdriver.Chrome()
# but_add = b.find_element_by_id("addbutton2v2-1023-btnInnerEl")
# but_add.click()

# ------------------------------------------------


# from selenium import webdriver

# driver = webdriver.Chrome(executable_path=r'C:\bin\chromedriver.exe')
# driver.get('http://www.wp.pl')
# title = driver.title
# print(title)
# assert 'Demobank - Bankowosc Internetowa - Logowanie' == title
# driver.quit()

#-----------------------------------------------------------------------------

# import unittest
# from selenium import webdriver

# class MainTests(unittest.TestCase):
# def test_demo_login(self):
# driver = webdriver.Chrome(executable_path=r"C:\bin\chromedriver.exe")
# driver.get('https://demobank.jaktestowac.pl/logowanie_etap_1.html')
# title = driver.title
# print(title)
# assert 'Demobank - Bankowosc Internetowa - Logowanie' == title
# driver.quit()

