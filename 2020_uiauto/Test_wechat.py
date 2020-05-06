from time import sleep

from appium import webdriver


class Test_wechat:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "lin"
        caps["appPackage"] = "com.tencent.mm"
        caps["appActivity"] = ".ui.LauncherUI"
        caps["autoGrantPermissions"] = "true"
        caps['noReset'] = True
        # caps["unicodeKeyboard"] = True  # 设置输入中文之后重置输入法
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)  # 定义为实例变量
        self.driver.implicitly_wait(5)  # 增加隐式等待

    def test_sendmessage(self):
        self.driver.find_element_by_xpath("//*[contains(@resource-id,'b1t') and contains(@index,'10')]").click()
        for x in range(0, 100):
            x += 1
            self.driver.find_element_by_id("ajs").send_keys("s")
            self.driver.find_element_by_id("amb").click()
            self.driver.find_element_by_id("ajs").send_keys("k")
            self.driver.find_element_by_id("amb").click()
            self.driver.find_element_by_id("ajs").send_keys("y")
            self.driver.find_element_by_id("amb").click()
            self.driver.find_element_by_id("ajs").send_keys("s")
            self.driver.find_element_by_id("amb").click()
    def teardown(self):
        pass
        # self.driver.quit()
