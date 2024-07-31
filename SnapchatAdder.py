from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os

# 可以实现加好友并发第一条消息,没写下滑 python SnapchatAdder.py


options = UiAutomator2Options().load_capabilities({
"platformName": "Android",
    "platformVersion": "10",
    "deviceName": "4304927d",
    "appActivity": "com.snapchat.android.LandingPageActivity",
    "appPackage": "com.snapchat.android",
    "autoGrantPermissions": True,
    "noReset": True,
    "fullReset": False,
    "disableIdLocatorAutocompletion": True,
    "uiautomator2ServerInstallTimeout": 60000,  # 设置超时时间为 60 秒
    # "skipServerInstallation":True,
    # 'skipDeviceInitialization': True,
    # 'automationName': 'UiAutomator1'


})

message = input("What message you want to send to people: ")

def click_element(driver,element_id,type=AppiumBy.ID):
    element = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((type, element_id))
  
)
    element.click()

    
def type_element(driver,element_id,text):
    element = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((AppiumBy.ID, element_id))
  
)
    element.click()
    element.send_keys(text)

    

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

#click_element(driver,"com.snapchat.android:id/hova_header_add_friend_icon")

#scu_added_me_chat number m
while(True):
    click_element(driver,"com.snapchat.android:id/hova_header_add_friend_icon")


    try:
        view_more_button_id = 'new UiSelector().resourceId("add_friends_view_more_cell")'
        click_element(driver, view_more_button_id, AppiumBy.ANDROID_UIAUTOMATOR)
    except:
        continue

    #limit times
    for i in range(1,4):
        m = i-1
        click_element(driver,f"(//android.widget.Button[@content-desc=\"Accept\"])[1]",AppiumBy.XPATH)
        sleep(5)
        
    
        # msgButton = driver.find_elements(AppiumBy.ID,"scu_added_me_chat")
        
        # msgButton[m].click()
        msg_buttons = driver.find_elements(AppiumBy.ID, "scu_added_me_chat")
        # click first one scu added chat
        j = 0
        msg_buttons[j].click()
        print(m)
        


        sleep(5)
      
        type_element(driver,"com.snapchat.android:id/chat_input_text_field",message)
        driver.press_keycode(66) 
        sleep(5)
        click_element(driver,"com.snapchat.android:id/back_button")
    driver.press_keycode(4)
