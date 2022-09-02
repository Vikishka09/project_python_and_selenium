from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_shopping_cart(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def book_was_added_to_shopping_cart(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        book_name_on_alert = self.browser.find_element(*ProductPageLocators.BOOK_NAME_ON_ALERT)
        assert book_name.text == book_name_on_alert.text, \
            f'Another book has been added to the cart {book_name.text}'

    def checking_value_of_shopping_cart(self):
        basket_sum = self.browser.find_element(*ProductPageLocators.BASKET_SUM)
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        assert basket_sum.text == book_price.text, \
            f'The amount of purchases is not equal to the cost of the book {book_price.text}'
