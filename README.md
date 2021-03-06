# ps5-bot
 This is a fork of a PS5 bot made by https://github.com/MMZaini updated for Israel stores: Ivory and alsale - this bot doesnt automatically type in your credit card info and purchase the whole thing for you, it only keeps refreshing until its avaliable and when its avaliable, it adds to cart and takes you to checkout, you have to input your details when making a purchase into the website.

# credits
  - https://github.com/azaini101
    He created the original bot which was made for walmart in the US, i used it to convert it for the UK
  - https://github.com/MMZaini/ps5-uk-bot
	I changed it for Israeli stores :)

# requirements
  - python 3.6 or higher; Install latest at https://www.python.org/downloads/
  - latest google chrome version (version 88.0+) - check your chrome version chrome://settings/help and update to latest if needed. - If you dont already have google chrome installed, install at https://www.google.com/intl/en_uk/chrome/
  - latest chrome driver for chrome version 88; this can be installed at https://chromedriver.chromium.org/downloads
  - any sort of unzipping program, i'd recommend installing winrar since its free and easy to use
  -- If you dont meet any single one of these requirements, the program will NOT work
  
# required modules
  - Selenium - installable by typing 'pip install selenium' into the command prompt. Make sure you install everything above, in the requirements.
  -- If you dont install selenium, the program will NOT work
  
# instructions
  1. Install the included, zipped, python program - it should be in your downloads folder, you can drag it over to your desktop or anywhere else if you'd like.
  2. Locate and unzip 'ps5-uk-bot-main.zip' using winrar by right clicking the zip and selecting 'Extract Here'
  3. Open the new folder that can be found in the same directory that you have the zip in when unzipping.
  4. You can now delete the zip since its no longer needed but make sure you keep the folder.
  5. Open the folder and copy the chromedriver you installed to the folders, you want to copy it into the 'digital ps5 bots' folder and into the 'disk ps5 bots'. Then double click the chromedriver and you'll see a little command prompt looking window come up. (make sure you open the chromedriver which is in the same folder as whichever store you want to bot) It'll say something like Starting ChromeDriver, Only local connections are allowed and ChromeDriver was started successfully. If you see somehting like this on the window you've comleted the hard part.
  6. Insert user/pass into the run.ini file, each section represents a store (ivory/alsale)
  7. Minimise the chromedriver into your taskbar and double click the file for whichever store you want to bot and digital or disk. It'll then bring up another command prompt looking window which should say something like 'DevTools listening'. Then It'll open chrome and depending on the performance (speed) of your computer, it'll refresh the page constantly until the ps5 is avaliable for to be added to cart and purchasesd, when it is avaliable, it will add to cart and take you straight to the checkout page and make a beep sound to alert you to the availbility of the item. Then you'd just checkout normally.
  
# things to keep in mind
  - Ivory and alsale dont require you to either login or create an account to make a purchase, sbut it might be a good idea to open one, the bot can use your cardentials to login to facilitate the move to the checkout page

# common errors
  - "chromedriver.exe' executable needs to be in PATH." -- You can fix this error by closing chromedriver if you have it open, then find where the chromedriver.exe and put it into your desktop. Then put the .py file for whichever store you want onto your desktop too. then double click the chromedriver. Then double click the .py and it should work
  - "please specify a unique value for --user-data-dir argument, or don't use --user-data-dir" -- You can fix this by closing all other chrome tabs you may have. Remember: You can only have 1 bot open at a time (you can change this, check # customisability)

# customisability
  -- Keep in mind, if you want to customise or change the code and use it your self, make sure to read the license before doing anything --  
  - You can make it so you have multiple bots open at the same time, here are some instructions.
  
  1. Open the files of the bots you want to have open at the same time in a code editor
  2. find where it says "options.add_argument" then check the whole line and go to where it says 'ps5'  
  3. change the ps5 to something else, it needs to be different for each file for it to work. (you may need  to put each file in a seperate folder and copy chromedriver into each folder and run it from each folder if its still not working)
  - You can really easily change the item you want to bot, here are some instructions on how to do it. (you only need common sense for this and make sure you read the license before distrubuting it!)
  
    1. Open the included .py program for whichever store you want to change the item for in your prefered code editor, such as VScode, Sublime Text, ect (you can use notepad or python idle but its not recommended)
    2. Find the 'item' variable, it's on line 6 from the top. Change the link inside the apostrophes (the '') to the link of the item you want to bot!

