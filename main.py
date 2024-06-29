from appium import webdriver as app
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time
import math

def start_app(driver, app_package, app_activity):
    driver.start_activity(app_package, app_activity)
    
    
def close_app(driver):
    action = TouchAction(driver)
    action.press(x=563, y=2674).move_to(x=587, y=2041).release().perform()
    time.sleep(6)
    TouchAction(driver).tap(x=619, y=2448).perform()

def main():
    app1 = {
    "platformName": "Android",
    "appium:platformVersion": "14",
    "appium:deviceName": "A4YQVB3223012816",
    "appium:appPackage": "com.manmanbuy.bijia",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "com.manmanbuy.bijia.StartActivity",
    "appium:noReset": "false",
    }

    app2 = {
        "platformName": "Android",
        "platformVersion": "14",
        "deviceName": "A4YQVB3223012816",
        "appPackage": "com.tencent.mm",
        "appActivity": "com.tencent.mm.ui.LauncherUI",
        "automationName": "UiAutomator2",
        "noReset": "true",
    }

    appium_server = 'http://localhost:4723/wd/hub'

    # 启动第一个应用
    driver = app.Remote(appium_server, app1)
    time.sleep(5)
    TouchAction(driver).tap(x=970,y=2037).perform()
    time.sleep(5)
    TouchAction(driver).tap(x=961,y=2559).perform()
    time.sleep(2)
    
    driver.press_keycode(3)
    
    # 切换到第二个应用
    start_app(driver, app2["appPackage"], app2["appActivity"])
    time.sleep(10)

    # 截屏
    driver.get_screenshot_as_file('screen.png')

    # 执行点击操作
    TouchAction(driver).tap(x=722, y=2534).perform()
    time.sleep(2)
    TouchAction(driver).tap(x=610, y=2046).perform()
    time.sleep(2)
    TouchAction(driver).tap(x=162, y=605).perform()
    time.sleep(2)
    TouchAction(driver).tap(x=1136, y=199).perform()
    time.sleep(2)
    
    
    close_app(driver)
    driver.quit()

if __name__ == '__main__':
    for i in range(2):
        try:
            main()
        except Exception as e:
            print(e)
            continue

