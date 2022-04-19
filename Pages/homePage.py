# страница пользовательского профиля
from selenium.webdriver.common.by import By
from Locators.locators import Locators


class HomePage:

    def __init__(self, driver):
        self.driver = driver

        self.welcome_xpath = Locators.welcome_xpath
        self.click_my_orders_xpath = Locators.click_my_orders_xpath
        self.click_my_favorite_xpath = Locators.click_my_favorite_xpath
        self.click_personal_data_xpath = Locators.click_personal_data_xpath
        self.click_register_card_xpath = Locators.register_card_xpath
        self.edit_personal_data_css_selector = Locators.edit_personal_data_css_selector
        self.contact_info_css_selector = Locators.contact_info_css_selector
        self.address_info_message_css_selector = Locators.address_info_message_css_selector
        self.subscribe_message_css_selector = Locators.subscribe_message_css_selector
        self.subscribe_email_message_xpath = Locators.subscribe_email_message_xpath
        self.subscribe_sms_message_xpath = Locators.subscribe_sms_message_xpath
        self.change_password_link_text = Locators.change_password_link_text
        self.new_password_name = Locators.new_password_name
        self.old_password_name = Locators.old_password_name
        self.confirmation_new_password_name = Locators.confirmation_new_password_name
        self.click_save_changes_name = Locators.save_changes_name
        self.click_basket_xpath = Locators.basket_xpath
        self.catalog_products_xpath = Locators.catalog_products_xpath


        # self.exit_link_text = Locators.exit_link_text
        # self.new_products_xpath = Locators.new_products_xpath
        # self.sale_xpath = Locators.sale_xpath
        # self.discounts_and_bonuses_xpath = Locators.discounts_and_bonuses_xpath
        # self.payment_and_delivery_xpath = Locators.payment_and_delivery_xpath
        # self.hurry_up_xpath = Locators.hurry_up_xpath
        # self.contacts_xpath = Locators.contacts_xpath
        # self.airsoft_guns_xpath = Locators.airsoft_guns_xpath
        # self.all_guns_xpath = Locators.all_guns_xpath
        # self.pyrotechnics_xpath = Locators.pyrotechnics_xpath
        # self.all_guns_xpath_2 = Locators.all_guns_xpath_2
        # self.link_vk_xpath = Locators.link_vk_xpath
        # self.link_facebook_xpath = Locators.link_facebook_xpath
        # self.link_twitter_xpath = Locators.link_twitter_xpath
        # self.link_instagram_xpath = Locators.link_instagram_xpath
        # self.link_youtube_xpath = Locators.link_youtube_xpath
        # self.link_telegram_bot_xpath = Locators.link_telegram_bot_xpath
        # self.email_us_css_selector = Locators.email_us_css_selector
        # self.close_the_form_css_selector = Locators.close_the_form_css_selector
        # self.articles_xpath = Locators.articles_xpath
        # self.top_logo_css_selector = Locators.top_logo_css_selector
        # self.button_buy_vint1_xpath = Locators.button_buy_vint1_xpath

    def check_welcome_message(self):
        msg = self.driver.find_element(By.XPATH, self.welcome_xpath).text
        return msg

    def click_my_orders(self):
        self.driver.find_element(By.XPATH, self.click_my_orders_xpath).click()

    def click_my_favorite(self):
        self.driver.find_element(By.XPATH, self.click_my_favorite_xpath).click()

    def click_personal_data(self):
        self.driver.find_element(By.XPATH, self.click_personal_data_xpath).click()

    def click_register_card(self):
        self.driver.find_element(By.XPATH, self.click_register_card_xpath).click()

    def click_edit_personal_data(self):
        msg_9 = self.driver.find_element(By.CSS_SELECTOR, self.edit_personal_data_css_selector).click()
        return msg_9

    def contact_info_message(self):
        msg_10 = self.driver.find_element(By.CSS_SELECTOR, self.contact_info_css_selector).text
        return msg_10

    def delivery_info_message(self):
        msg_11 = self.driver.find_element(By.CSS_SELECTOR, self.address_info_message_css_selector).text
        return msg_11

    def other_subscribe_message(self):
        msg_12 = self.driver.find_element(By.CSS_SELECTOR, self.subscribe_message_css_selector).text
        return msg_12

    def subscribe_email_message(self):
        msg_13 = self.driver.find_element(By.XPATH, self.subscribe_email_message_xpath).click()
        return msg_13

    def subscribe_sms_message(self):
        msg_14 = self.driver.find_element(By.XPATH, self.subscribe_sms_message_xpath).click()
        return msg_14

    def click_change_password(self):
        self.driver.find_element(By.LINK_TEXT, self.change_password_link_text).click()

    def old_password_value(self):
        self.driver.find_element(By.NAME, self.old_password_name).clear()
        self.driver.find_element(By.NAME, self.old_password_name)

    def new_password_value(self):
        self.driver.find_element(By.NAME, self.new_password_name).clear()
        self.driver.find_element(By.NAME, self.new_password_name)

    def confirmation_new_password_value(self):
        self.driver.find_element(By.NAME, self.confirmation_new_password_name).clear()
        self.driver.find_element(By.NAME, self.confirmation_new_password_name)

    def click_save_changes(self):
        self.driver.find_element(By.NAME, self.click_save_changes_name).click()

    def click_basket(self):
        self.driver.find_element(By.XPATH, self.click_basket_xpath).click()

    def click_catalog_products(self):
        self.driver.find_element(By.XPATH, self.catalog_products_xpath).click()
    #
    # def click_exit(self):
    #     self.driver.find_element(By.LINK_TEXT, self.exit_link_text).click()
    #



    #
    # def click_new_products(self):
    #     self.driver.find_element(By.XPATH, self.new_products_xpath).click()
    #
    # def click_sale(self):
    #     self.driver.find_element(By.XPATH, self.sale_xpath).click()
    #
    # def click_discounts_and_bonuses(self):
    #     self.driver.find_element(By.XPATH, self.discounts_and_bonuses_xpath).click()
    #
    # def click_payment_and_delivery(self):
    #     self.driver.find_element(By.XPATH, self.payment_and_delivery_xpath).click()
    #
    # def click_hurry_up(self):
    #     self.driver.find_element(By.XPATH, self.hurry_up_xpath).click()
    #
    # def click_contacts(self):
    #     self.driver.find_element(By.XPATH, self.contacts_xpath).click()
    #
    # def click_airsoft_guns(self):
    #     self.driver.find_element(By.XPATH, self.airsoft_guns_xpath).click()
    #
    # def click_all_guns(self):
    #     self.driver.find_element(By.LINK_TEXT, self.all_guns_xpath).click()
    #
    # def click_pyrotechnics(self):
    #     self.driver.find_element(By.XPATH, self.pyrotechnics_xpath).click()
    #
    # def click_all_guns_2(self):
    #     self.driver.find_element(By.XPATH, self.all_guns_xpath_2).click()
    #
    # def click_link_vk(self):
    #     self.driver.find_element(By.XPATH, self.link_vk_xpath).click()
    #
    # def click_link_facebook(self):
    #     self.driver.find_element(By.XPATH, self.link_facebook_xpath).click()
    #
    # def click_link_twitter(self):
    #     self.driver.find_element(By.XPATH, self.link_twitter_xpath).click()
    #
    # def click_link_instagram(self):
    #     self.driver.find_element(By.XPATH, self.link_instagram_xpath).click()
    #
    # def click_link_youtube(self):
    #     self.driver.find_element(By.XPATH, self.link_youtube_xpath).click()
    #
    # def click_link_telegram_bot(self):
    #     self.driver.find_element(By.XPATH, self.link_telegram_bot_xpath).click()
    #
    # def click_email_us(self):
    #     self.driver.find_element(By.CSS_SELECTOR, self.email_us_css_selector).click()
    #
    # def click_close_the_form(self):
    #     self.driver.find_element(By.CSS_SELECTOR, self.close_the_form_css_selector).click()
    #
    # def click_articles(self):
    #     self.driver.find_element(By.XPATH, self.articles_xpath).click()
    #
    # def click_top_logo(self):
    #     self.driver.find_element(By.CSS_SELECTOR, self.top_logo_css_selector).click()
    #
    # def click_button_buy_vint1(self):
    #     self.driver.find_element(By.XPATH, self.button_buy_vint1_xpath).click()
