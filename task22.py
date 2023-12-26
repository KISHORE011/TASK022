from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# Set the path to your ChromeDriver executable
serv_obj=Service("C:\z.selenium drivers\chromedriver-win64\chromedriver.exe")

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=serv_obj)

# Maximize the browser window
driver.maximize_window()

# guvi's instagram url
driver.get("https://www.instagram.com/guviofficial/")

act=ActionChains(driver)
# Wait for the page to load (you may need to adjust the wait time based on your network speed)
driver.implicitly_wait(7)

driver.find_element(By.LINK_TEXT,'Log in').click()

###########################   GIVE YOUR OWN USERNAME AND PASSWORD OF INSTAGRAM ACCOUNT ("WITH IN DOUBLE QUOTATION MARK")  #####################################

# login steps

username=("")
password=("")

driver.find_element(By.NAME,'username').send_keys(username)
driver.find_element(By.NAME,'password').send_keys(password)

time.sleep(7)
#  click login
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]').click()

time.sleep(7)
driver.find_element(By.LINK_TEXT, 'Search').click()
time.sleep(7)
(driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input').send_keys('guviofficial'))

time.sleep(10)
act.send_keys(Keys.ARROW_DOWN).perform()
time.sleep(6)
act.send_keys(Keys.ENTER).perform()

time.sleep(7)
# open the followers list
act.send_keys(Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB).perform()
time.sleep(6)
act.send_keys(Keys.ENTER).perform()
time.sleep(7)
# Close the followers list
act.send_keys(Keys.TAB).perform()
act.send_keys(Keys.ENTER).perform()

# Extract the total number of followers
followers=(driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a/span').get_attribute("title"))
print("Followers:", followers)

# Wait for the following list to load
driver.implicitly_wait(10)

time.sleep(7)
# open the following list
act.send_keys(Keys.TAB).perform()
act.send_keys(Keys.ENTER).perform()
time.sleep(6)
# Close the followers list
act.send_keys(Keys.TAB).perform()
act.send_keys(Keys.ENTER).perform()

# Extract the total number of following                                                                                                                                    #the following value is none "==0"
following = (driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a/span/span').get_attribute('title'))

if following:
    print("Following: ", following)

else:
    print("Following: 4 ")

time.sleep(7)
# Close the browser
driver.close()

