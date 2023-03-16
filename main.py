from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys #sending keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains #actionchains for repeated usability
from selenium.webdriver.chrome.service import Service #service for the webdriver
from selenium.webdriver.common.by import By #locating elements by...
from selenium.webdriver.support import expected_conditions as EC #expected conditions - explicit waits


service = Service(r'C:\Users\paulk\Desktop\Selenium\chromedriver.exe')
driver = webdriver.Chrome(service=service)



class SpotworkAutoTest():
    def setUp(self):
        self.driver = webdriver.Chrome(r'C:\Users\paulk\Desktop\Selenium\chromedriver.exe')
        self.driver.get("https://spot-ef0ee.web.app/checkins")

        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "email"))
            )
        finally:
            driver.quit()
        
        #email_address = driver.find_element(By.ID, "email")
        #email_address.click()

        text_input = driver.find_element(By.ID, "email")
        initialSetup = ActionChains(driver)
        initialSetup.click(on_element=text_input)
        initialSetup.send_keys("koushik@spotwork.co")
       
        #to let you actually see things
        time.sleep(10)



    ###

    def tearDown(self):
        self.driver.close()


#actually running everything
spotAuto = SpotworkAutoTest()
spotAuto.setUp()
spotAuto.tearDown()




