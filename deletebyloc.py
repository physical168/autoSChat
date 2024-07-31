from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os

# 导航栏点击map后启动,可实现删除搜索区的巴基斯坦人

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
    "uiautomator2ServerInstallTimeout": 60000  # 设置超时时间为 60 秒
})

# message = input("What message you want to send to people: ")

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


def contains_pakistan(s):
    if "Pakistan" in s:
        return True
    else:
        return False

# # 测试示例
# test_string1 = "I love visiting Pakistan."
# test_string2 = "I have never been to India."

# print(contains_pakistan(test_string1))  # 输出: True
# print(contains_pakistan(test_string2))  # 输出: False

def deletefriend():
    # 点击 unified_profile_icon_button_action_menu 按钮
    action_menu_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((AppiumBy.ID, "unified_profile_icon_button_action_menu"))
            )
    action_menu_button.click()
    # 点击 Manage Friendship 按钮
    manage_friendship_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((AppiumBy.XPATH, "//android.view.View[@resource-id='com.snapchat.android:id/action_sheet_cell' and .//javaClass[@text='Manage Friendship']]"))
            )
    manage_friendship_button.click()
    # 点击 Remove Friend 按钮
    removed_friend_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((AppiumBy.XPATH, "//android.view.View[@resource-id='com.snapchat.android:id/action_sheet_cell' and .//javaClass[@text='Remove Friend']]"))
            )
    removed_friend_button.click()
    #点击remove
    specific_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((AppiumBy.XPATH, "//android.view.View[@index='1' and @clickable='true' and @text='' and @bounds='[171,1244][909,1423]']"))
            )
    specific_button.click()

    

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)


try:
    # 获取页面源代码
    # print(driver.page_source)
    # 点击地图界面搜索键
    click_element(driver, "com.snapchat.android:id/hova_header_search_icon")
    sleep(3)
    driver.press_keycode(4)

    
    users = driver.find_elements(AppiumBy.XPATH, "//android.view.View[@resource-id='friend-on-map-result-cell']")
    
    for user in users:
        subtitle_element = user.find_element(AppiumBy.XPATH, ".//android.widget.TextView[@resource-id='result-subtitle']")
        subtitle_text = subtitle_element.get_attribute("text")
        
        if contains_pakistan(subtitle_text):

            avatar_element = user.find_element(AppiumBy.XPATH, ".//android.view.View[@resource-id='avatar']")
            # 带蓝圈要长按 没写
            avatar_element.click()
            
            # 进一步的操作，比如发送消息
            

            sleep(5)
            # click_element(driver, "com.snapchat.android:id/back_button")
            deletefriend()
            print(driver.page_source)
            driver.press_keycode(4)
            sleep(5)

    driver.press_keycode(4)  # 返回按钮，返回到前一个屏幕
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()


# print(driver.page_source)
#python deletebyloc.py
