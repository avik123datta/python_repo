import pytest
from selenium import webdriver
import time
class Test_actitime():
    @pytest.fixture(scope="module")
    def setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="D:\Andy\chromedriver\chromedriver.exe")
        driver.get("http://demo.actitime.com")
        yield driver
        driver.close()

    @pytest.mark.parametrize("user,passw",[("raju","gentleman"),("admin","manager")])
    def test_login(self,setup,user,passw):
        #time.sleep(2)
        driver.find_element_by_xpath("//input[@name='username']").send_keys("admin")
        driver.find_element_by_xpath("//input[@name='pwd']").send_keys("manager")
        #time.sleep(2)

		
		
        driver.find_element_by_id("loginbutton").click()
