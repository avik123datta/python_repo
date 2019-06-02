import pytest
from selenium import webdriver
import time
class Test_actitime():
    @pytest.fixture(scope="module")
    def setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="D:\Andy\chromedriver\chromedriver.exe")
        driver.get("http://demo.actitime.com")
        driver.maximize_window()
        yield driver
        #driver.close()

    @pytest.mark.parametrize("user,passw",[("raju","gentleman"),("admin","manager")])
    def test_login(self,setup,user,passw):
        time.sleep(2)
        username = driver.find_element_by_xpath("//input[@name='username']")
        time.sleep(2)
        username.clear()
        username.send_keys(user)
        time.sleep(3)
        password = driver.find_element_by_xpath("//input[@name='pwd']")
        time.sleep(2)
        password.clear()
        password.send_keys(passw)
        #time.sleep(2)
        driver.find_element_by_id("loginButton").click()




