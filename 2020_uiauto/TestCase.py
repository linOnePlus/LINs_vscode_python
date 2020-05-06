import datetime
import time

import pytest
import yaml
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.extensions.android.gsm import GsmCallActions
from selenium.webdriver.support.wait import WebDriverWait


class TestCase:
    yaml_parm = yaml.safe_load(open("search.yaml","r"))
    print(yaml_parm)
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "lin"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = "true"
        caps["unicodeKeyboard"] = True  # 设置输入中文之后重置输入法
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
        el3.send_keys("阿里巴巴")
        time.sleep(5)
        el3.clear()
        el3.send_keys("google")
        el4 = self.driver.find_element_by_id("com.xueqiu.android:id/stockName")
        el4.click()

    def test_gsm_call(self):
        self.driver.make_gsm_call("13691802995", GsmCallActions.CALL)
        self.driver.send_sms("8615999549759", "sb")

    def test_xianshi01(self):
        # len()有问题？   要用 find_elements_by_id（）才是返回一个数组
        def load():
            print(datetime.datetime.now())
            if len(self.driver.find_elements_by_id("tv_agree")) >= 1:
                return True
            else:
                return False

        WebDriverWait(self.driver, 20).until(load())
        self.driver.find_element_by_id("tv_agree").click()

    def test_xianshi02(self):
        time.sleep(20)
        if len(self.driver.find_element_by_id("tv_agree")) >= 1:
            self.driver.find_element_by_id("tv_agree").click()

    def test_xianshi03(self):
        WebDriverWait(self.driver, 20).until(
            lambda x: len(self.driver.find_elements_by_id("com.xueqiu.android:id/tv_agree")) >= 1)
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_agree").click()

    def test_xapth(self):
        targe = self.driver.find_element_by_xpath("//*[contains(@resource-id,'tv_agree') and contains(@text,'同意')] ")
        targe.click()

    def test_assert(self):
        assert len(self.driver.find_elements_by_id("com.xueqiu.android:id/tv_agree")) >= 1
        print("pass01")
        assert "同" in self.driver.find_element_by_id("com.xueqiu.android:id/tv_agree").get_attribute("text")
        print("pass02")

    @pytest.mark.parametrize("keyword,keycode", [("google", 1001), ("alibaba", 1002)])
    def test_parm(self, keyword, keycode):
        el2 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_agree")
        el2.click()
        self.driver.find_element_by_id("tv_search").click()
        el1 = self.driver.find_element_by_id("search_input_text")
        el1.send_keys(keyword)
        time.sleep(5)
        el1.clear()
        el2 = self.driver.find_element_by_id("search_input_text")
        el2.send_keys(keycode)

    @pytest.mark.parametrize("keyword,keycode", yaml_parm)
    def test_yaml(self,keyword,keycode):
        el2 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_agree")
        el2.click()
        self.driver.find_element_by_id("tv_search").click()
        el1 = self.driver.find_element_by_id("search_input_text")
        el1.send_keys(keyword)
        time.sleep(5)
        el1.clear()
        el2 = self.driver.find_element_by_id("search_input_text")
        el2.send_keys(keycode)

    def teardown(self):
        pass
        # self.driver.quit()
