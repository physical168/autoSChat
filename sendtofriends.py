from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from time import sleep

options = UiAutomator2Options().load_capabilities({
    "platformName": "Android",
    "platformVersion": "12",
    "deviceName": "adb-AUWXVB1318007545-20lwpU._adb-tls-connect._tcp",
    "appActivity": "com.snapchat.android.LandingPageActivity",
    "appPackage": "com.snapchat.android",
    "autoGrantPermissions": True,
    "noReset": True,
    "fullReset": False,
    "disableIdLocatorAutocompletion": True,
})

message = input("What message you want to send to people: ")

def click_element(driver, element_id, type=AppiumBy.ID):
    try:
        element = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((type, element_id))
        )
        element.click()
    except TimeoutException:
        print(f"TimeoutException: Element with ID '{element_id}' not found or not clickable")
        print(driver.page_source)
        raise
    except NoSuchElementException:
        print(f"NoSuchElementException: Element with ID '{element_id}' not found")
        print(driver.page_source)
        raise

def type_element(driver, element_id, text):
    try:
        element = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((AppiumBy.ID, element_id))
        )
        element.click()
        element.send_keys(text)
    except TimeoutException:
        print(f"TimeoutException: Element with ID '{element_id}' not found or not clickable")
        print(driver.page_source)
        raise
    except NoSuchElementException:
        print(f"NoSuchElementException: Element with ID '{element_id}' not found")
        print(driver.page_source)
        raise

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

def send_message_to_friend(driver, friend_name):
    try:
        # 点击聊天图标
        click_element(driver, "com.snapchat.android:id/hova_header_chat_icon")

        # 查找名为 friend_name 的好友
        friends = WebDriverWait(driver, 30).until(
            EC.presence_of_all_elements_located((AppiumBy.ID, "com.snapchat.android:id/friend_name"))
        )

        friend_found = False
        for friend in friends:
            if friend.text == friend_name:
                friend.click()
                friend_found = True
                break

        if not friend_found:
            print(f"Friend named '{friend_name}' not found")
            return

        # 发送消息
        type_element(driver, "com.snapchat.android:id/chat_input_text_field", message)
        driver.press_keycode(66)  # Press Enter key to send the message

        # 返回到好友列表
        driver.press_keycode(4)
    except Exception as e:
        print(f"An error occurred while sending message to friend: {e}")

# 给名为 Pong Ka 的朋友发送消息
send_message_to_friend(driver, "Pong Ka")
