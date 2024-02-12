import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class HomePageTest(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome()
        driver = cls.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        driver.implicitly_wait(15)

    def test_search_text_field(self):
        driver = self.driver
        search_field = driver.find_element(By.ID, 'search')
        search_field.clear()

        search_field.send_keys('hola')
        search_field.submit()
        #Anda

    def test_search_text_field_by_name(self):
        search_field = self.driver.find_element(By.NAME, 'q')
        search_field.clear()

        search_field.send_keys('hola')
        search_field.submit()
        #Anda

    def test_search_text_field_by_class_name(self):
        search_field = self.driver.find_element(By.CLASS_NAME, 'input-text')
        search_field.clear()

        search_field.send_keys('dasdsads')
        search_field.submit()
        #Anda

    def test_search_button_ennabled(self): 
        button = self.driver.find_element(By.CLASS_NAME, 'button')
        #Anda

    def test_count_of_promo_banner_images(self):
        banner_list = self.driver.find_element(By.CLASS_NAME, 'promos')
        banners = banner_list.find_elements(By.TAG_NAME, 'img')
        self.assertEqual(3, len(banners))
        #Anda

    def test_vip_promo(self):
        vip_promo = self.driver.find_element(By.XPATH, '//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[4]/a/img')
        #Anda

    def test_shopping_cart(self):
        shopping_cart_icon = self.driver.find_element(By.CSS_SELECTOR, "div.header-minicart span.icon")
    def tearDown(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity = 2)