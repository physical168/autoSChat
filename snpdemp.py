from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

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

message = input("What message you want to send to people: ")

def click_element(driver, element_id, type=AppiumBy.ID):
    element = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((type, element_id))
    )
    element.click()

def type_element(driver, element_id, text):
    element = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((AppiumBy.ID, element_id))
    )
    element.click()
    element.send_keys(text)

def tap_screen(driver, x, y):
    actions = {
        "action": "tap",
        "options": {
            "x": x,
            "y": y
        }
    }
    driver.execute_script("mobile: performEditorAction", actions)

try:
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

    while True:
        click_element(driver, "com.snapchat.android:id/hova_header_add_friend_icon")
        for i in range(1, 4):
            m = i - 1

            # 点击添加并发消息
        # click acceptAS
            click_element(driver,f"(//android.widget.Button[@content-desc=\"Accept\"])[1]",AppiumBy.XPATH)
            sleep(15)

            # 点击scu_quick_add_chat，屏幕坐标为x=704,y=851
            tap_screen(driver, 704, 851)
            sleep(2)  # 确保点击后界面稳定

            # 输入消息并发送
            type_element(driver, "com.snapchat.android:id/chat_input_text_field", message)
            driver.press_keycode(66)  # 发送消息
            click_element(driver, "com.snapchat.android:id/back_button")

        driver.press_keycode(4)  # 返回主界面

finally:
    driver.quit()
