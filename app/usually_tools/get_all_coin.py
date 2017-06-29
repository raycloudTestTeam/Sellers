import unittest
from app.page.driver_start import *
from time import sleep
from app.page.dingtalk import *

class ALLCOIN(object):

    def __init__(self):
        self.driver = Driver("http://erp103.tongtool.com/myaccount/exchangerate/index.htm","HtmlUnit").start()
        self.driver.maximize_window()
        name = self.driver.find_element_by_name("username")
        name.send_keys("362116814@qq.com")
        password = self.driver.find_element_by_name("password")
        password.send_keys("123456")
        self.driver.find_element_by_class_name("l_btn").click()
        sleep(3)

    def get_coin(self,coins):

        div = self.driver.find_element_by_id("showExchangeRate")
        table = div.find_elements_by_tag_name("table")[1]
        trs = table.find_elements_by_tag_name("tr")
        for index in range(1, len(trs)):
            tds = trs[index].find_elements_by_tag_name("td")
            key = tds[1].text
            value  = tds[2].text
            coins[key]=value
        return coins

    def get_all_coin(self):
        try:
            coins = {}
            re = self.get_coin(coins)
            page = self.driver.find_element_by_class_name("pages")
            page.find_elements_by_tag_name("a")[1].click()
            sleep(2)
            re_1 = self.get_coin(re)
            ding_talk(str(re_1),0)
            return u"抓取货币成功"
        except:
            ding_talk(str("抓取货币失败"),0)


if __name__ == "__main__":
    unittest.main(verbosity=2)