from selenium.common.exceptions import NoSuchElementException
from pages.base_pages import BasePage as B


class DemoQa(B):

    def exist_icon(self):
        try:
            B.find_element(locator='#app>header>a')
        except NoSuchElementException:
            return False
        return True










