# Test case
# -----------------------------------------------------------------
# 1.	Open web browser (Chrome/Firefox/Edge).
# 2.	Open URL: https://admin-demo.nopcommerce.com/login
# 3.	Enter Email (admin@yourstore.com).
# 4.	Enter Password (admin).
# 5.	Click on Login.
# 6.	Capture title of the home page. (Actual title)
# 7.	Verify title of the page: Dashboard / nopCommerce administration (Expected)
# 8.	Close browser.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service("D:\Software\Browser Drivers\Chrome\chromedriver.exe")
driver=webdriver.Chrome(service= serv_obj)

driver.get("https://admin-demo.nopcommerce.com/login")
driver.find_element(By.NAME,"Email").clear()
driver.find_element(By.NAME,"Email").send_keys("admin@yourstore.com")

driver.find_element(By.ID,"Password").clear()
driver.find_element(By.ID,"Password").send_keys("admin")
driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button").click()

act_title=driver.title
exp_title="Dashboard / nopCommerce administration"

if act_title==exp_title:
    print("Login test Passed")
else:
    print("Login Test Failed")

driver.close()
