import inspect
import os
from playwright.sync_api import sync_playwright, Page, Browser
from dotenv import load_dotenv

load_dotenv()

# Логин и пароль
USERNAME = os.getenv("AVITO_USERNAME")
PASSWORD = os.getenv("AVITO_PASSWORD")

# создание папки, если её ещё нет
output_directory = "output"
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# xpath элементов для скриншотов
counters_xpath = {
    "all": "//div[@class='desktop-impact-items-F7T6E']",
    "water": "//div[@class='desktop-label-EIkG9' and text()='было сохранено']/../..",
    "co2": "//div[@class='desktop-label-EIkG9' and text()='не попало в атмосферу']/../..",
    "energy": "//div[@class='desktop-label-EIkG9' and text()='было сэкономлено']/../..",
}


class User:
    def __init__(self, auth=False) -> None:
        """Функция инициализации пользователя"""
        self.auth = auth

    def __enter__(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)
        self.page: Page = self.browser.new_page()

        if self.auth:
            self.authenticate(self.page)

        self.page.goto("https://www.avito.ru/avito-care/eco-impact")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.browser.close()
        self.playwright.stop()

    def authenticate(self, page: Page) -> None:
        """
        Функция для аутентификации на сайте.
        """
        page.goto("https://www.avito.ru/#login?authsrc=h")
        page.wait_for_load_state()
        page.fill('input[name="login"]', USERNAME)
        page.fill('input[name="password"]', PASSWORD)
        page.click('button[type="submit"]')
        input(
            "Выполните необходимые действия. Решите капчу/введите код из смс-уведомления. После этого нажмите Enter"
        )

    def take_screenshot_with_xpath(self, element_xpath: str, id_test: str):
        calling_frame = inspect.stack()[1]
        function_name = calling_frame.function
        element = self.page.wait_for_selector(element_xpath)
        if element:
            auth = self.auth
            # Делаем скриншот элемента
            element.screenshot(path=f"{output_directory}/{id_test}{function_name}_{auth=}.png")

    # блок тестов
    def test_saved_counter_all(self, id_test: str):
        xpath = counters_xpath['all']
        self.take_screenshot_with_xpath(xpath, id_test)

    def test_saved_counter_co2(self, id_test: str):
        xpath = counters_xpath["co2"]
        self.take_screenshot_with_xpath(xpath, id_test)

    def test_saved_counter_water(self, id_test: str):
        xpath = counters_xpath["water"]
        self.take_screenshot_with_xpath(xpath, id_test)

    def test_saved_counter_energy(self, id_test: str):
        xpath = counters_xpath["energy"]
        self.take_screenshot_with_xpath(xpath, id_test)


def test_unauthenticated_user():
    with User(auth=False) as unauthenticated_user:
        unauthenticated_user.test_saved_counter_all('T1')
        unauthenticated_user.test_saved_counter_co2('T2')
        unauthenticated_user.test_saved_counter_water('T3')
        unauthenticated_user.test_saved_counter_energy('T4')


def test_authenticated_user():
    with User(auth=True) as authenticated_user:
        authenticated_user.test_saved_counter_all('T5')
        authenticated_user.test_saved_counter_co2('T6')
        authenticated_user.test_saved_counter_water('T7')
        authenticated_user.test_saved_counter_energy('T8')
