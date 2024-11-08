from selenium.webdriver.common.by import By
from test1.utils.base_page import BasePage

class ProductsPage(BasePage):
    FIRST_PRODUCT_NAME = (By.CSS_SELECTOR, ".inventory_item_name")
    FIRST_PRODUCT_PRICE = (By.CSS_SELECTOR, ".inventory_item_price")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn_inventory")
    CART_BUTTON = (By.CSS_SELECTOR, ".shopping_cart_link")

    def get_first_product_details(self):
        name = self.find_element(self.FIRST_PRODUCT_NAME).text
        price = self.find_element(self.FIRST_PRODUCT_PRICE).text
        return name, price

    def add_first_product_to_cart(self):
        self.click_element(self.ADD_TO_CART_BUTTON)

    def go_to_cart(self):
        self.click_element(self.CART_BUTTON)
