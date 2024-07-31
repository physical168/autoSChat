from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.interaction import Interaction
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from time import sleep
from selenium.webdriver.common.by import By


# python deleteif.py
# 直接从好友列表开始删

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
    "uiautomator2ServerInstallTimeout": 1200000 ,   # 设置超时时间为 1200 秒
    # 'automationName': 'UiAutomator2',

    # "skipServerInstallation":True,
    # 'skipDeviceInitialization': True,
})

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

def contains_pakistan(s):
    return "Pakistan" in s

def contains_india_or_pakistan(text):
    """
    This function checks if the given text contains the words "India" or "Pakistan".
    
    Args:
    text (str): The text to check.
    
    Returns:
    bool: True if the text contains "India" or "Pakistan", otherwise False.
    """
    return "India" in text or "Pakistan" in text

def deletefriend():
    action_menu_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((AppiumBy.ID, "unified_profile_icon_button_action_menu"))
    )
    
    action_menu_button.click()
    sleep(1)
    manage_friendship_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((AppiumBy.XPATH, "//android.view.View[@resource-id='com.snapchat.android:id/action_sheet_cell' and .//javaClass[@text='Manage Friendship']]"))
    )
    manage_friendship_button.click()
    sleep(1)
    removed_friend_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((AppiumBy.XPATH, "//android.view.View[@resource-id='com.snapchat.android:id/action_sheet_cell' and .//javaClass[@text='Remove Friend']]"))
    )
    removed_friend_button.click()
    sleep(3)
    
    try:
        print(1)
        fourline_button = WebDriverWait(driver, 30).until(
        
         # 四行
        EC.element_to_be_clickable((AppiumBy.XPATH, "//android.view.View[@index='1' and @clickable='true' and @text='' and @bounds='[171,1244][909,1423]']"))
        
        )
        fourline_button.click()
    
    except Exception as e:
        threeline_button = WebDriverWait(driver, 30).until(
        
            # 这里严格坐标,试试能不能改了用范围写   好像要长按一秒 或者double click  三行                                                                                                          
            EC.element_to_be_clickable((AppiumBy.XPATH, "//android.view.View[@index='1' and @clickable='true' and @text!='Cancel' and @bounds='[171,1198][909,1377]']"))
        )
        threeline_button.click()
        
    
    sleep(3)



#获得屏幕大小宽和高
def getSize(driver):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)
 
#屏幕向上滑动
def swipeUp(driver,t=1000):
    l = getSize(driver)
    x1 = int(l[0] * 0.5)    #x坐标
    y1 = int(l[1] * 0.75)   #起始y坐标
    y2 = int(l[1] * 0.25)   #终点y坐标
    driver.swipe(x1, y1, x1, y2,t)

# 好友列表滑动
def swipeFriendListUp(driver,t=1000):
    l = getSize(driver)
    x1 = int(l[0] * 0.5)    #x坐标
    y1 = int(l[1] * 0.90)   #起始y坐标
    y2 = int(l[1] * 0.25)   #终点y坐标
    driver.swipe(x1, y1, x1, y2,t)


#屏幕向下滑动
def swipeDown(driver,t=1000):
    l = getSize(driver)
    x1 = int(l[0] * 0.5)  #x坐标
    y1 = int(l[1] * 0.25)   #起始y坐标
    y2 = int(l[1] * 0.75)   #终点y坐标
    driver.swipe(x1, y1, x1, y2,t)
#屏幕向左滑动
def swipLeft(driver,t):
    l=getSize(driver)
    x1=int(l[0]*0.75)
    y1=int(l[1]*0.5)
    x2=int(l[0]*0.05)
    driver.swipe(x1,y1,x2,y1,t)
#屏幕向右滑动
def swipRight(driver,t=1000):
    l=getSize(driver)
    x1=int(l[0]*0.05)
    y1=int(l[1]*0.5)
    x2=int(l[0]*0.75)
    driver.swipe(x1,y1,x2,y1,t)

# 点击进个人对话框之后判断是否是要删除的国家并删除
def deletebyloc():
    # Find all conversation_subtext_view elements
    conversation_views = driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.snapchat.android:id/conversation_subtext_view']")

    # Iterate through each conversation_subtext_view element
    for view in conversation_views:
        text = view.get_attribute("text")
    
    # Use the function to check if the text contains "India" or "Pakistan"
        if contains_india_or_pakistan(text):
            print("Found:", text)
            # You can perform additional actions here if needed
            # Locate the FrameLayout element by resource ID
            # 点名字不点头像
            # avatar_icon = driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='com.snapchat.android:id/avatar_icon']")

            # # Perform a click action on the element
            # avatar_icon.click()

            # Locate the TextView element by resource ID and text
            conversation_title = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.snapchat.android:id/conversation_title_text_view']")

            # Perform a click action on the element
            conversation_title.click()

            deletefriend()
        
            # 返回两人聊天界面
            print("返回两人聊天界面")
            driver.press_keycode(4)
            sleep(2)

            #去掉输入框
            # print("去掉输入")
            # driver.press_keycode(4)
            # sleep(3)

            

        else:
            # print("Not found:", text)
            print("Not found")
    

 
def click_all_friends(driver):
    while True:
        # friends = driver.find_elements(AppiumBy.XPATH, "//android.view.View[@index='1']//javaClass[@package='com.snapchat.android' and contains(@text, '')]")
        # friends = driver.find_elements(AppiumBy.XPATH, "//android.view.View[@index='0']//javaClass[contains(@text, '') and @package='com.snapchat.android']")
        friends = driver.find_elements(AppiumBy.XPATH, 
    "//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.view.View[javaClass and not(javaClass[@text='Best Friends']) and not(javaClass[starts-with(@text, '&#x') or string-length(@text)=1])]")


        if not friends:
            break

        

        for friend in friends:

            friend_name_element = friend.find_element(AppiumBy.CLASS_NAME, "javaClass")
            friend_name = friend_name_element.get_attribute("text")
            # print(friend_name)

            # 获取好友项的坐标
            location = friend_name_element.location
            y_coordinate = location['y']

            
            #  获取好友名称
            # friend_name = friend.find_element(AppiumBy.CLASS_NAME, "javaClass").get_attribute("text")

             
            # 验证好友名称和Y坐标
            if friend_name and y_coordinate > 400:
                # 点击好友项
                print("Found friends:")
                print(friend_name)
                print(y_coordinate)
                sleep(2)
            
                friend.click()
                sleep(3)  # 可以根据需要调整
                deletebyloc()
                #退出输入框
                driver.press_keycode(4)
                # 退出两人聊天界面
                driver.press_keycode(4)
            
        swipeUp(driver)
        sleep(2)
        # print(1)







driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

click_all_friends(driver)

driver.quit()
# print(driver.page_source)
# python deleteif.py
