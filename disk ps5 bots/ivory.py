import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from base import selenium_init

# ------------------------------
# ivory:
# ------------------------------
class ivory(selenium_init):
    def __init__(self) -> None:
        selenium_init.__init__(self, ivory.__name__)

    def test_ivory(self):
        self.driver.set_window_size(960, 784)
        self.driver.find_element(By.LINK_TEXT, "כניסה").click()
        self.driver.find_element(By.ID, "mail").click()
        self.driver.find_element(By.ID, "mail").send_keys(self.user)
        self.driver.find_element(By.ID, "pass").send_keys(self.pss)
        self.driver.find_element(By.ID, "btn-invitation").click()

    # ------------------------------
    # run_bot: 
    # ------------------------------
    def run_bot(self):
        item = self.url.replace("$id", self.id) # Variable for the item wanted
        print (item)
        self.driver.get(item)
        while True:
            try:
                self.driver.find_element(By.CSS_SELECTOR, ".col-sm-6 > #fastBuy").click() # Looks for the 'add to cart button' using xpath
            except:
                time.sleep(self.sleep)
                self.print_debug(item)
                self.driver.get(item) # If the atc button cannot be found, refresh until it is found
            else:
                time.sleep(1)
                self.test_ivory()
                break
        self.play_sound()
        if self.send_email:
            self.send_email(msg = "GO to ivory at: https://www.ivory.co.il/CheckOutUpsells.aspx?auction_id=%s&f=1" % self.id, shop_name = "ivory")

# --------
# main:
# --------
if(__name__ == "__main__"):
    print("This program comes with ABSOLUTELY NO WARRANTY; for details check included license. This is free software, and you are welcome to redistribute it under certain conditions; check license for conditions.")
    o = ivory()
    o.run_bot()
