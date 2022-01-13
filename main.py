# LOGIN & CLICK!! - Here we're doing a Login into a website & then clicking a specific button o the next page

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains


#  we create a function for getting all the drivers for our webpage

def get_driver():  
  
  # driver = webdriver.Chrome()
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument('start-maximized')
  options.add_argument('disable-dev-shm-usage')
  options.add_argument('no-sandbox')
  options.add_experimental_option('excludeSwitches',['enable-automation'])
  options.add_argument('diable-blink-features=AutomationControlled')
  # NOTE: We've to mention the options variable as options, becaues it is a positional argument
  driver = webdriver.Chrome(options = options)
  # connecting our driver to a specific webpage
  url = 'https://app.mrinsta.com/login'
  driver.get(url)
  return driver

# driver = get_driver()
def clean_text(text):
  inp = text.split(':')[1]
  output = int(inp.split('/')[0])
  return output



def main():
  while True:
    # getting our driver
    driver = get_driver()
    #  with this driver we extract an element using it's CSS id and .send_keys press the given string as input keys via console keybord

    # Entering username
    driver.find_element(by='xpath',value='/html/body/section/div/div/div/div[2]/div[2]/form/div[2]/input').send_keys("YOUR INSTAGRAM USERNAME")
    #  Delay 2 secs
    time.sleep(2)
    # Enter Password & Pressing the 'Enter/Return' Key
    driver.find_element(by='xpath',value='/html/body/section/div/div/div/div[2]/div[2]/form/div[3]/input').send_keys(+"YOUR INSTAGRAM PASSWORD" Keys.RETURN)
    # Click the ACTIVATE Button
    driver.find_element(by= "xpath",value= "/html/body/section/div/div/div/div[2]/div[3]/div/div[1]/div/div/div/form/div[2]/button").click()

    # while (follow_count <= 10):
    #   follow_conf = driver.find_element(by='xpath', value='/html/body/section/div/div/div/div[1]/div[2]/div[1]/p').text
    #   follow_count = clean_text(follow_conf)
    for i in range(0,30):
      try:
        # click FOLLOW 
        driver.find_element(by= "xpath",value= "/html/body/section/div/div/div/div[1]/div[2]/div[3]/div[2]/div[1]/a").click()
        # print(driver.current_url)
        time.sleep(10)
        # Switch to the new window and open URL B
        driver.switch_to.window(driver.window_handles[1])
        # driver.get(tab_url)
        # print(driver.current_url)
        # p = driver.current_window_handle
        # driver.switch_to.window(p)
        driver.close()
        # time.sleep(10)
        driver.switch_to.window(driver.window_handles[0])
        print(driver.current_url)
        # # driver.find_element(by="xpath", value ="/html/body").send_keys(Keys.CONTROL, 'q')

        # # ActionChains(driver) \
        # #   .key_down(Keys.CONTROL) \
        # #   .send_keys('w')  \
        # #   .key_up(Keys.CONTROL)  \
        #   .perform()
        # time.sleep(2)
        # # cur_win = get_Current_window()
        # driver.switch_to.window(cur_win)
        # time.sleep(0.9)
        # print("Child window title: " + driver.title)
        # driver.quit()
        #  click CONFIRM
        driver.find_element(by= "xpath", value= "/html/body/section/div/div/div/div[1]/div[2]/div[3]/div[2]/div[2]/form/button" ).click()
        time.sleep(10)
      except Exception as e:
        print("The Exception is: ", e)
    
    driver.find_element(by="xpath", value="/html/body/section/div/div/div/div[1]/div[2]/div/form/button").click()
    time.sleep(24*60*60)
 






print(main())
