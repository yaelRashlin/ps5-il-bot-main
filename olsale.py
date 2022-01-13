import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from base import selenium_init, send_email

# ------------------------------
# olsale:
# ------------------------------
class olsale(selenium_init):
    def __init__(self) -> None:
        selenium_init.__init__(self, olsale.__name__)

    # ------------------------------
    # test_pass:
    # ------------------------------
    def test_pass(self):
        self.driver.find_element(By.ID, "txtUserName").click()
        self.driver.find_element(By.ID, "txtUserName").send_keys(self.user)
        self.driver.find_element(By.ID, "txtPassword").send_keys(self.pss)
        self.driver.find_element(By.ID, "loginBtn").click()

    # ------------------------------
    # run_bot: 
    # ------------------------------
    def run_bot(self):
        item = self.url.replace("$id", self.id) # Variable for the item wanted
        self.driver.get(item)
        while True:
            try:
                self.driver.find_element(By.XPATH, '//a[@id=\'BuyBtnfixed\']/span').click() # Looks for the 'add to cart button' using xpath
            except:
                time.sleep(self.sleep)
                self.print_debug(item)
                self.driver.get(item) # If the atc button cannot be found, refresh until it is found
            else:
                time.sleep(1)
                self.test_pass()
                break
        self.play_sound() 
        send_email(msg = "GO to olsale at: https://www.olsale.co.il/CheckOutUpsells.aspx?auction_id=%s&f=1" % self.id, shop_name = "olsale")


# --------
# main:
# --------
if(__name__ == "__main__"):
    print("This program comes with ABSOLUTELY NO WARRANTY; for details check included license. This is free software, and you are welcome to redistribute it under certain conditions; check license for conditions.")
    o = olsale()
    o.run_bot()