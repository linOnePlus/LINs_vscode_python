from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestCase:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "lin"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = "true"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)  # 定义为实例变量
        self.driver.implicitly_wait(10)  # 增加隐式等待

    def test_demo(self):
        el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_agree")
        el1.click()
        # action = TouchAction(driver)
        # action.press(200,300)
        el2 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        el2.click()
        el3 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        el3.send_keys("google")
        el4 = self.driver.find_element_by_id("com.xueqiu.android:id/stockName")
        el4.click()

    def teardown(self):
        self.driver.quit()
