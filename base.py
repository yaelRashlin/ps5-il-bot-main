from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import configparser as configparser
import os
import smtplib
from datetime import date
import playsound
import winsound
import os

file_loc = os.path.realpath(__file__)
script_dir = os.path.dirname(file_loc)

# ------------------------------
# selenium_init:
# ------------------------------
class selenium_init():
    def __init__(self, shop_name) -> None:
        self.options = Options()
        self.options.add_argument("user-data-dir=C:\\Users\\ps5\\AppData\\Local\\Google\\Chrome\\User Data\\%s" % shop_name)
        self.driver = webdriver.Chrome('chromedriver.exe', options = self.options)

        ini = os.path.join(script_dir, "run.ini" )
        self.config = configparser.ConfigParser()
        self.config.read(ini)

        self.user = self.config.get(shop_name, 'user')
        self.pss = self.config.get(shop_name, 'pass')
        self.url = self.config.get(shop_name, 'item_url')
        self.id = self.config.get(shop_name, 'id')
        self.sleep = int(self.config.get("general", 'sleep'))
        self.script_dir = script_dir

    # ------------------------------
    # print_debug: 
    # ------------------------------
    def print_debug(self, item):
        today = date.today()
        print("%s -> %s" % (today, item))

    # ------------------------------
    # play_sound: 
    # ------------------------------
    def play_sound(self):
        print ("Play Hallelujah :) ")
        # winsound.Beep(899, 5000) # Makes a beep sound for 5 seconds to notify the user that the item is in stock 
        playsound.playsound(os.path.join(self.script_dir, "The 8-bit Hallelujah Chorus.mp3" ), True)  

# ------------------------------
# send_email:
# ------------------------------
def send_email(msg = None, shop_name = None):
    print (msg)
    sender = 'yael.rashlin@gmail.com'
    receivers = ['yael.rashlin@gmail.com']
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(sender, "wxjozbveamvsdfxq")

    message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
MIME-Version: 1.0
Content-type: text/html
Subject: Found PS5 at %s

This is an e-mail message to be sent in HTML format

<b>This is HTML message.</b>
<h1>%s</h1>
""" % (shop_name, msg)

    server.sendmail(sender, sender, message)
    server.quit()