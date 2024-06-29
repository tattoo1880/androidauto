from appium import webdriver as app
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium.webdriver.common.proxy import Proxy, ProxyType

import time


def touchele(x,y):
    TouchAction(driver).tap(x=x, y=y).perform()
    time.sleep(2)
# 配置代理

desired_caps = {
    "platformName": "Android",
    "platformVersion": "14",
    "deviceName": "A4YQVB3223012816",
    "appPackage": "com.taobao.taobao",
    "appActivity": "com.taobao.tao.welcome.Welcome", 
    "automationName": "UiAutomator2",
    "noReset": "true",
    # "proxy": {
    #     "proxyType": "MANUAL",
    #     "httpProxy": "127.0.0.1:8080",
    #     "sslProxy": "127.0.0.1:8080"
    # }
}
    
# Appium 服务器地址
appium_server = f'http://localhost:4723/wd/hub'

# 连接到 Appium 服务器
driver = app.Remote(appium_server, desired_caps)

touchele(1090,185)
# click 1132.351
touchele(1132,351)
# click 111，794
touchele(139,794)
# click 503，1025
touchele(517,739)
touchele(342,1986)
touchele(970,776)
touchele(605,2000)




# 读取当前页面截屏



driver.quit()


