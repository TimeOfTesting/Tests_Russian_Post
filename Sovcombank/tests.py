from main_page import *
from coftest import *

text = 'Совкомбанк'


class TestSuite:

    def test_1(self, driver):
        """Поиск сайта 'Почта РФ' в поисковой системе браузера Google,
        печать в консоли количества найденных результатов"""
        google_page = GooglePage(driver)
        google_page.search('Почта РФ')
        google_page.print_search_results()

    def test_2(self, driver):
        """Открытие страницы сайта 'Почта РФ', переход на вкладку текущего сайта,
        закрытие вкладки поисковой системы"""
        google_page = GooglePage(driver)
        google_page.open_russian_post_website()

    def test_3(self, driver):
        """Открытие страницы аутентификации, проверка кликабельности кнопки 'Войти'
        и проверка пустоты полей 'Электронная почта или телефон', 'Пароль'"""
        page_authentication = RussianPostWebsitePageAuthentication(driver)
        page_authentication.click_login_button()
        page_authentication.authenticate()

    def test_4(self, driver):
        """Заполнение поля 'Электронная почта или телефон' невалидными значениеми,
        печать в консоль информационных сообщений об ошибках"""
        page_authentication = RussianPostWebsitePageAuthentication(driver)
        page_authentication.check_login_field('   ', '888a789!@!!!3435adasfas')

    def test_5(self, driver):
        """Переход на главную страницу сайта 'Почта РФ', осуществление поиска введеного значения по сайту,
        проверка сообщения о результате поиска"""
        page_home = RussianPostWebsiteHomePage(driver)
        page_home.go_to_home_page()
        page_home.perform_search(text)

    def test_6(self, driver):
        """Переход на главную страницу сайта 'Почта РФ',
        выбор в верхнем меню сайта в категории 'Отправить' вариант 'Посылку'"""
        page_menu_send = RussianPostWebsiteMenuSend(driver)
        page_menu_send.select_menu_send()

    def test_7(self, driver):
        """Создание словаря, где ключи: кнопки переключения раздела 'Куда',
        значения: прейсхолдер соотвествующего поля. Печать словаря в консоли"""
        page_menu_send = RussianPostWebsiteMenuSend(driver)
        page_menu_send.section_where_to_send()






