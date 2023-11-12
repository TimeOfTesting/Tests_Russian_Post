from selenium.webdriver.common.keys import Keys
from locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class BasePage:

    def __init__(self, driver):
        self.driver = driver

class GooglePage(BasePage):

    def search(self, query):
        with open('url_google.txt', 'r') as file:
            url = file.read()
            self.driver.get(url)
            input_google = self.driver.find_element(*GOOGLE.INPUT)
            input_google.send_keys(query)
            input_google.send_keys(Keys.ENTER)

    def print_search_results(self):
        result = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((*GOOGLE.RESULT_COUNT,)))
        print(result.text)

    def open_russian_post_website(self):
        website = self.driver.find_element(*GOOGLE.OPEN_RUSSIAN_POST_WEBSITE).click()
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        self.driver.close()
        all_windows = self.driver.window_handles
        new_window = self.driver.switch_to.window(all_windows[0])


class RussianPostWebsitePageAuthentication(BasePage):

    def click_login_button(self):
        login_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((*RUSSIAN_POST_WEBSITE_AUTHENTICATION.LOGIN_BUTTON,)))
        self.driver.execute_script("arguments[0].click();", login_button)

    def authenticate(self):
        button_authentication = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((*RUSSIAN_POST_WEBSITE_AUTHENTICATION.BUTTON_AUTHENTICATION,)))
        login_input = self.driver.find_element(*RUSSIAN_POST_WEBSITE_AUTHENTICATION.LOGIN_INPUT)
        password_input = self.driver.find_element(*RUSSIAN_POST_WEBSITE_AUTHENTICATION.PASSWORD_INPUT)

        assert button_authentication.is_displayed()
        assert login_input.get_attribute('value') == ''
        assert password_input.get_attribute('value') == ''

    def check_login_field(self, login_1, login_2):
        login = self.driver.find_element(*RUSSIAN_POST_WEBSITE_AUTHENTICATION.LOGIN_INPUT)
        login.click()
        login.send_keys(login_1)
        error = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((*RUSSIAN_POST_WEBSITE_AUTHENTICATION.LOGIN_INPUT_ERROR,)))
        time.sleep(3)
        print(f'Сообщение об ошибке при заполнении поля тремя пробелами: {error.text}')
        login.clear()
        login.send_keys(login_2)
        error = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((*RUSSIAN_POST_WEBSITE_AUTHENTICATION.LOGIN_INPUT_ERROR,)))
        print(f'Сообщение об ошибке при заполнении поля невалидными данными: {error.text}')

class RussianPostWebsiteHomePage(BasePage):

    def go_to_home_page(self):
        logo_home_page = self.driver.find_element(*RUSSIAN_POST_WEBSITE_HOME_PAGE.LOGO_HOME_PAGE).click()

    def perform_search(self, text):
        search_button_home_page = self.driver.find_element(*RUSSIAN_POST_WEBSITE_HOME_PAGE.SEARCH_BUTTON_HOME_PAGE)
        search_button_home_page.click()
        search_field = self.driver.find_element(*RUSSIAN_POST_WEBSITE_HOME_PAGE.SEARCH_FIELD)
        search_field.send_keys(text)
        search_field.send_keys(Keys.ENTER)
        time.sleep(5)
        search_field_error = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((*RUSSIAN_POST_WEBSITE_HOME_PAGE.SEARCH_FIELD_ERROR,)))
        assert f'Извините, по вашему запросу “{text}” ничего не найдено. Попробуйте изменить запрос или вернитесь на главную.' == search_field_error.text


class RussianPostWebsiteMenuSend(BasePage):

    def select_menu_send(self):
        back_to_home_page = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((*RUSSIAN_POST_WEBSITE_HOME_PAGE.GO_BACK_TO_HOME_PAGE,)))
        back_to_home_page.click()
        menu_send = self.driver.find_element(*RUSSIAN_POST_WEBSITE_MENU_SEND.MENU_SEND)
        actions = ActionChains(self.driver)
        actions.move_to_element(menu_send).perform()
        send_a_package = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((*RUSSIAN_POST_WEBSITE_MENU_SEND.SEND_A_PACKAGE,)))
        send_a_package.click()

    def section_where_to_send(self):

        result_dict = dict()

        radio_send_in_russia_element = self.driver.find_element(*RUSSIAN_POST_WEBSITE_MENU_SEND.RADIO_SEND_IN_RUSSIA)
        radio_send_in_russia = radio_send_in_russia_element.text

        send_in_russia_element = self.driver.find_element(*RUSSIAN_POST_WEBSITE_MENU_SEND.PLACEHOLDER_SEND_IN_RUSSIA)
        placeholder_send_in_russia = send_in_russia_element.get_attribute('placeholder')

        radio_to_send_another_country_element = self.driver.find_element(*RUSSIAN_POST_WEBSITE_MENU_SEND.RADIO_TO_SEND_ANOTHER_COUNTRY)
        self.driver.execute_script("arguments[0].scrollIntoView();", radio_to_send_another_country_element)
        radio_to_send_another_country_element.click()
        radio_to_send_another_country = radio_to_send_another_country_element.text

        send_another_country_element = self.driver.find_element(*RUSSIAN_POST_WEBSITE_MENU_SEND.PLACEHOLDER_TO_SEND_ANOTHER_COUNTRY)
        placeholder_to_send_another_country = send_another_country_element.get_attribute('placeholder')

        radio_send_by_phone_number_element = self.driver.find_element(*RUSSIAN_POST_WEBSITE_MENU_SEND.RADIO_SEND_BY_PHONE_NUMBER)
        radio_send_by_phone_number_element.click()
        radio_send_by_phone_number = radio_send_by_phone_number_element.text

        send_by_phone_number_element = self.driver.find_element(*RUSSIAN_POST_WEBSITE_MENU_SEND.PLACEHOLDER_SEND_BY_PHONE_NUMBER)
        placeholder_send_by_phone_number = send_by_phone_number_element.get_attribute('placeholder')

        radio_send_by_index_element = self.driver.find_element(*RUSSIAN_POST_WEBSITE_MENU_SEND.RADIO_SEND_BY_INDEX)
        radio_send_by_index_element.click()
        radio_send_by_index = radio_send_by_index_element.text


        send_by_index_to_element = self.driver.find_element(*RUSSIAN_POST_WEBSITE_MENU_SEND.PLACEHOLDER_SEND_BY_INDEX)
        placeholder_send_by_index = send_by_index_to_element.get_attribute('placeholder')


        result_dict[radio_send_in_russia] = placeholder_send_in_russia
        result_dict[radio_to_send_another_country] = placeholder_to_send_another_country
        result_dict[radio_send_by_phone_number] = placeholder_send_by_phone_number
        result_dict[radio_send_by_index] = placeholder_send_by_index

        print(result_dict)

