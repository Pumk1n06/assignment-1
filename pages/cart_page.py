from selenium.webdriver.common.by import By
from test1.utils.base_page import BasePage

class CartPage(BasePage):
    CART_ITEM_NAME = (By.CSS_SELECTOR, ".inventory_item_name")
    CART_ITEM_PRICE = (By.CSS_SELECTOR, ".inventory_item_price")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_BUTTON = (By.ID, "logout_sidebar_link")

    def get_cart_item_details(self):
        name = self.find_element(self.CART_ITEM_NAME).text
        price = self.find_element(self.CART_ITEM_PRICE).text
        return name, price

    def logout(self):
        self.click_element(self.MENU_BUTTON)
        self.click_element(self.LOGOUT_BUTTON)
