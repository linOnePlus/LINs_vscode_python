# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
# 这个是appium desktop自动生成的脚本 并不是测试用例
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

caps = {}
caps["platformName"] = "Android"
caps["deviceName"] = "lin"
caps["appPackage"] = "com.xueqiu.android"
caps["appActivity"] = ".view.WelcomeActivityAlias"
caps["autoGrantPermissions"] = "true"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(10)  # 增加隐式等待

el1 = driver.find_element_by_id("com.xueqiu.android:id/tv_agree")
el1.click()
# action = TouchAction(driver)
# action.press(200,300)
el2 = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
el2.click()
el3 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el3.send_keys("google")
el4 = driver.find_element_by_id("com.xueqiu.android:id/stockName")
el4.click()
driver.quit()
