# для фикстур
# python -m pytest -v --html=.\Reports\report.html --driver Chrome --driver-path D:/SkillFactory/FixPrice/chromedriver.exe Tests/login.py

from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.by import By
from Pages.loginPage import LoginPage
from Pages.homePage import HomePage
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.service = Service()
        cls.driver = webdriver.Chrome(executable_path='D:/SkillFactory/FixPrice/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01_invalid_username_message(self):
        """Ввод неверного логина"""
        driver = self.driver
        driver.get('https://fix-price.ru/personal/')

        driver.find_element(By.XPATH, "//label[@for='switcher-auth__email']").click()
        login = LoginPage(driver)
        login.enter_username('6arikov80mail.ru')
        login.enter_password('Kruglik0v85')
        login.click_login()
        login.check_invalid_username_message()
        message = driver.find_element(By.XPATH, '//div[@class="form-line auth-result"]').text
        self.assertEqual(message, 'Email введен некорректно')


    def test_02_invalid_password_message(self):
        """Ввод неверного пароля"""
        driver = self.driver

        driver.find_element(By.XPATH, "//label[@for='switcher-auth__email']").click()
        login = LoginPage(driver)
        login.enter_username('6arikov85@mail.ru')
        login.enter_password('1234567')
        login.click_login()
        login.check_invalid_password_message()
        time.sleep(3)
        message_2 = driver.find_element(By.XPATH, '//div[@class="form-line auth-result"]').text
        self.assertEqual(message_2, 'Пользователь с таким логином и паролем не найден.')


    def test_03_invalid_username_and_password_message(self):
        """Ввод неверных логина и пароля"""
        driver = self.driver

        driver.find_element(By.XPATH, "//label[@for='switcher-auth__email']").click()
        login = LoginPage(driver)
        login.enter_username('6arikov80@mail.ru')
        login.enter_password('Kruqwe11rt')
        login.click_login()
        login.check_invalid_password_message()
        time.sleep(3)
        message_3 = driver.find_element(By.XPATH, '//div[@class="form-line auth-result"]').text
        self.assertEqual(message_3, 'Пользователь с таким логином и паролем не найден.')


    def test_04_login_valid(self):
        """Ввод верных логина и пароля"""
        driver = self.driver

        driver.find_element(By.XPATH, "//label[@for='switcher-auth__email']").click()
        login = LoginPage(driver)
        login.enter_username('6arikov85@mail.ru')
        login.enter_password('Kruglik0v85')
        login.click_login()
        time.sleep(3)
        message_4 = driver.find_element(By.XPATH, '//div[@class="personal-info__greeting"]').text
        self.assertEqual(message_4, 'ЗДРАВСТВУЙТЕ,')

    def test_05_click_my_orders(self):
        """Проверка кликабельности кнопки 'Избранные товары'"""
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_my_orders()

        time.sleep(3)
        message_6 = driver.find_element(By.XPATH, '//a[@href="#orders"]').text
        self.assertEqual(message_6, 'МОИ ЗАКАЗЫ')

    def test_06_click_my_favorite(self):
        """Проверка кликабельности кнопки 'Избранное'"""
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_my_favorite()

        time.sleep(3)
        message_7 = driver.find_element(By.XPATH, '//a[@href="#favorites"]').text
        self.assertEqual(message_7, 'ИЗБРАННОЕ')

    def test_07_click_personal_data(self):
        """Проверка кликабельности кнопки 'Личные данные'"""
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_personal_data()

        message_8 = driver.find_element(By.XPATH, '//a[@class="js-lk-personal-tab"]').text
        self.assertEqual(message_8, 'ЛИЧНЫЕ ДАННЫЕ')

    def test_08_click_register_card(self):
        """Проверка кликабельности кнопки 'Зарегистрировать карту FIX-PRICE'"""
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_register_card()

        message_9 = driver.find_element(By.XPATH, '//a[@class="js-register-card-show"]').text
        self.assertEqual(message_9, 'ЗАРЕГИСТРИРОВАТЬ КАРТУ FIX PRICE')


    def test_09_click_edit_personal_data(self):
        """Проверка кликабельности кнопки 'Редактировать личные данные'"""
        driver = self.driver
        driver.find_element(By.XPATH, '//i[@class="icon icon-home"]').click()

        homepage = HomePage(driver)
        homepage.click_edit_personal_data()

        message_9 = driver.find_element(By.CSS_SELECTOR, "#home > div:nth-child(1) > div > div.personal-info__client > a").text
        self.assertEqual(message_9, '')

    def test_10_contact_info_message(self):
        """Наличие контактной информации в моем профиле"""
        driver = self.driver

        message_10 = driver.find_element(By.CSS_SELECTOR, "#personal_form > div:nth-child(6)").text
        self.assertEqual(message_10, 'ЛИЧНЫЕ ДАННЫЕ\nПОЛ\nЖЕНСКИЙ\nМУЖСКОЙ\nИЗМЕНИТЬ ПАРОЛЬ')

    def test_11_address_info_message(self):
        """Наличие информации об адресе в моем профиле"""
        driver = self.driver

        message_11 = driver.find_element(By.CSS_SELECTOR, "#personal_form > div:nth-child(7) > h5.uppercase").text
        self.assertEqual(message_11, 'АДРЕС')

    def test_12_subscribe_message(self):
        """Наличие графы подписка в моем профиле"""
        driver = self.driver

        message_11 = driver.find_element(By.CSS_SELECTOR, "#personal_form > div:nth-child(7) > h5:nth-child(4)").text
        self.assertEqual(message_11, 'ПОДПИСКА')

    def test_13_subscribe_email_message(self):
        """Проверка кликабельности кнопки подписки email в моем профиле"""
        driver = self.driver

        message_12 = driver.find_element(By.XPATH, '//label[@for="emailSubscribe"]').text
        self.assertEqual(message_12, '')

    def test_14_subscribe_sms_message(self):
        """Проверка кликабельности кнопки подписки sms в моем профиле"""
        driver = self.driver

        message_13 = driver.find_element(By.XPATH, '//label[@for="smsSubscribe"]').text
        self.assertEqual(message_13, '')

    def test_15_click_change_password(self):
        """Проверка кликабельности кнопки 'Изменить пароль'"""
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_change_password()

        message_14 = driver.find_element(By.LINK_TEXT, 'ИЗМЕНИТЬ ПАРОЛЬ').text
        self.assertEqual(message_14, 'ИЗМЕНИТЬ ПАРОЛЬ')

    def test_16_old_password_value(self):
        """Наличие поля 'Старый пароль' в графе изменить пароль"""
        driver = self.driver

        message_15 = driver.find_element(By.NAME, 'UF_TEMP_PASS').text
        self.assertEqual(message_15, '')

    def test_17_new_password_value(self):
        """Наличие поля 'Новый пароль' в графе изменить пароль"""
        driver = self.driver

        message_16 = driver.find_element(By.NAME, 'NEW_PASSWORD').text
        self.assertEqual(message_16, '')

    def test_18_confirmation_new_password_value(self):
        """Наличие поля 'Подтверждение пароля' в графе изменить пароль"""
        driver = self.driver

        message_17 = driver.find_element(By.NAME, 'NEW_PASSWORD_CONFIRM').text
        self.assertEqual(message_17, '')

    def test_19_click_save_changes(self):
        """Проверка кликабельности кнопки 'Сохранить изменения' в моём профиле"""
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_save_changes()

        message_18 = driver.find_element(By.NAME, 'save').text
        self.assertEqual(message_18, '')

    # def test_20_click_basket(self):
    #     """Проверка кликабельности кнопки 'В корзине'"""
    #     driver = self.driver
    #
    #     homepage = HomePage(driver)
    #     homepage.click_basket()
    #
    #     message_19 = driver.find_element(By.XPATH, '//*[@id="basketCounter"]').text
    #     self.assertEqual(message_19, 'Корзина')
    def test_20_click_catalog_products(self):
        """Проверка выпадающего списка при нажатие на каталог товаров"""
        driver = self.driver
        driver.find_element(By.XPATH, '//i[@class="icon icon-home"]').click()

        homepage = HomePage(driver)
        homepage.click_catalog_products()

        # product = [
        #     ]

        message_20 = driver.find_elements(By.XPATH, '//nav[@class="catalog-nav"]')
        self.assertEqual(message_20, '')





    @classmethod
    def tearDownClass(cls):
            cls.driver.close()
            cls.driver.quit()
            print('Test completed')

    if __name__ == '__main__':
        unittest.main()