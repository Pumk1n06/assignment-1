import unittest
from selenium import webdriver
from test1.pages.login_page import LoginPage
from test1.pages.products_page import ProductsPage
from test1.pages.cart_page import CartPage

class TestAddToCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        self.login_page = LoginPage(self.driver)
        self.products_page = ProductsPage(self.driver)
        self.cart_page = CartPage(self.driver)

    def test_add_to_cart(self):
        # Step 1: Login
        self.login_page.login("standard_user", "secret_sauce")

        # Step 2: Verify successful login (Products page)
        self.assertIn("inventory.html", self.driver.current_url, "Failed to login and navigate to Products page")

        # Step 3: Get first product name and price, save to file
        product_name, product_price = self.products_page.get_first_product_details()
        with open("product_details.txt", "w") as file:
            file.write(f"Product Name: {product_name}\nProduct Price: {product_price}")

        # Step 4: Add product to cart
        self.products_page.add_first_product_to_cart()

        # Step 5: Go to cart and verify product details
        self.products_page.go_to_cart()
        cart_name, cart_price = self.cart_page.get_cart_item_details()
        self.assertEqual(product_name, cart_name, "Product name does not match")
        self.assertEqual(product_price, cart_price, "Product price does not match")

        # Step 6: Logout
        self.cart_page.logout()
        self.assertIn("saucedemo.com", self.driver.current_url, "Failed to log out and navigate back to the homepage")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
