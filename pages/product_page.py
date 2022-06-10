from selenium.common.exceptions import NoAlertPresentException
from .base_page import BasePage
from .locators import ProductPageLocators
import math

class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()
		

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "No button to add to basket"
		
    def should_be_price_of_item(self):
        assert self.is_element_present(*ProductPageLocators.ITEM_PRICE), "No price of item"

    def should_be_name_of_item(self):
        assert self.is_element_present(*ProductPageLocators.ITEM_NAME), "No name of item"


    def should_be_alert_of_successfull_adding(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_SUCCESS_ADDING), "No message of successfull adding"

    def item_name_should_be_in_alert_of_successfull_adding(self):
        name1=self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        name2=self.browser.find_element(*ProductPageLocators.ALERT_SUCCESS_ADDING).text
        
        assert name1==name2, "Item name not in message of successfull adding"


    def should_be_price_of_added_item(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_OF_ADDED_ITEM), "No price of added item"

    def prices_should_be_equal(self):
        price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        price_of_added_item = self.browser.find_element(*ProductPageLocators.PRICE_OF_ADDED_ITEM).text
        print ("price=",price)
        print ("price_of_added_item", price_of_added_item)
        assert price_of_added_item == price, "Prices not equal"



    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")