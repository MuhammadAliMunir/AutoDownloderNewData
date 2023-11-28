from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from fake_useragent import UserAgent
import random
import time
import urllib
from bs4 import BeautifulSoup



def login(driver,wait):
    # wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div[3]/div[2]/div[1]/div/div/input'))).click()
    searchBar = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="header_username"]')))
    searchBar.clear()
    searchBar.send_keys("yuhengw")
    searchBar = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="header_password"]')))
    searchBar.clear()
    searchBar.send_keys("4p6%O@J*O9unefq")
    wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="header_desktop_user_menu_login"]'))).click()
    time.sleep(5)
def downloadImage(driver,wait,img):
    elem = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/main/div/div[2]/div[3]/div[2]/div/div/div['+str(img)+']/span[4]/a')))
    datSource = elem.get_attribute('data-resource')
    datSource = datSource.split('/')
    datSource = datSource[-1]
    # print(datSource)
    print(elem.get_attribute('data-resource'))
    elem.click()
    time.sleep(4)
    driver.switch_to.window(driver.window_handles[1])
    # print(driver.current_url)
    img = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/img')))
    img.screenshot("images/"+datSource)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])



    # time.sleep(30)
 
def ScrollPage(driver,speed = 100):
    # scrollHight = driver.execute_script("return document.body.scrollHeight;")
    scrollHight = 500
    # print(scrollHight)
    totalScroll = int(scrollHight/speed)
    randomScroll = random.randint(0,totalScroll)
    totalScrollDown = randomScroll * speed
    # print('totalScrol Down: '+str(totalScrollDown)) 
    for i in range(randomScroll):
        # print('down')
        scrollDownSleep = random.randint(0,1)
        time.sleep(scrollDownSleep)
        driver.execute_script("window.scrollBy(0, "+str(speed)+");")
    # scrollBackWait = random.randint(0,2)
    # time.sleep(scrollBackWait)
    while totalScrollDown > -1:
        # print('up:'+str(totalScrollDown))
        scrollUpSleep = random.randint(0,1)
        time.sleep(scrollUpSleep)
        driver.execute_script("window.scrollTo(0, "+str(totalScrollDown)+");")
        totalScrollDown = totalScrollDown - speed
    driver.execute_script("window.scrollTo(0, 0);")
    driver.execute_script("window.scrollTo(0, 0);")
    # time.sleep(10)
def ScrollPageDown(driver,speed = 100):
    driver.execute_script("window.scrollBy(0, "+str(speed)+");")


def getDriver(name):
    
    options = Options()
    # options.add_extension(pluginfile)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-infobars") #// disabling infobars

    driver = webdriver.Chrome( chrome_options=options)
    # driver = webdriver.Chrome()
    return driver

def start():
    driver = getDriver(name="")
    driver.get("https://avbrief.com")
    wait = WebDriverWait(driver, 8)
    login(driver,wait)
    ScrollPageDown(driver,200)
    wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="home_shortcut_uk_low_level_button"]'))).click()
    counter = 2
    checker = True
    while counter <= 5 and checker == True:
        try:
            downloadImage(driver,wait,counter)
        except:
            checker = False
        counter = counter + 1
    driver.quit()



    



start()
