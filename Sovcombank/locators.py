from selenium.webdriver.common.by import By

class GOOGLE:
    INPUT = (By.CSS_SELECTOR, 'textarea#APjFqb')
    OPEN_RUSSIAN_POST_WEBSITE = (By.CSS_SELECTOR, 'a[jsname="UWckNb"][href="https://www.pochta.ru/"]')
    RESULT_COUNT = (By.CSS_SELECTOR, 'div#result-stats')

class RUSSIAN_POST_WEBSITE_AUTHENTICATION:
    LOGIN_BUTTON = (By.XPATH, "//div[@class='Box-sc-7ax6ia-0 cquGUr']//a[text()='Войти']")
    BUTTON_AUTHENTICATION = (By.XPATH, '//button[@class="Buttonstyles__ButtonWrapper-sc-o9c5ps-1 lgVEbG"]//span[text()="Войти"]')
    LOGIN_INPUT = (By.CSS_SELECTOR, 'input#username')
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'input#userpassword')
    LOGIN_INPUT_ERROR = (By.CSS_SELECTOR, 'div#usernameError span')

class RUSSIAN_POST_WEBSITE_HOME_PAGE:
    LOGO_HOME_PAGE = (By.CSS_SELECTOR, 'a.sc-beqWaB.kyGAyu.header__logo[href="https://www.pochta.ru"]')
    SEARCH_BUTTON_HOME_PAGE = (By.CSS_SELECTOR, 'svg[role="button"]')
    SEARCH_FIELD = (By.CSS_SELECTOR, 'input[placeholder="Поиск по сайту"]')
    SEARCH_FIELD_ERROR = (By.CSS_SELECTOR, 'div.Notificationstyles__NotificationContent-sc-af5gun-3.kvktwS')
    GO_BACK_TO_HOME_PAGE = (By.CSS_SELECTOR, 'a[href="/"]')

class RUSSIAN_POST_WEBSITE_MENU_SEND:
    MENU_SEND = (By.XPATH, "//a[text()='Отправить']")
    SEND_A_PACKAGE = (By.XPATH, "//span[text()='Посылку']")
    RADIO_SEND_IN_RUSSIA = (By.XPATH, '//span[text()="По России"]')
    RADIO_TO_SEND_ANOTHER_COUNTRY = (By.XPATH, '//span[text()="В другую страну"]')
    RADIO_SEND_BY_PHONE_NUMBER = (By.XPATH, '//span[text()="По номеру телефона"]')
    RADIO_SEND_BY_INDEX = (By.XPATH, '//span[text()="По индексу"]')
    PLACEHOLDER_SEND_IN_RUSSIA = (By.CSS_SELECTOR, 'textarea#addressTo')
    PLACEHOLDER_TO_SEND_ANOTHER_COUNTRY = (By.CSS_SELECTOR, 'div.SelectControlstyles__InputWrapper-sc-1nv0s80-6.gxraQS input')
    PLACEHOLDER_SEND_BY_PHONE_NUMBER = (By.CSS_SELECTOR, 'input#phoneTo')
    PLACEHOLDER_SEND_BY_INDEX = (By.CSS_SELECTOR, 'input#indexTo')




