import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains



class TestView_product(unittest.TestCase): 

    @classmethod
    def setUpClass(cls): 
        cls.browser = webdriver.Chrome(ChromeDriverManager().install())
        cls.browser.maximize_window()

    # test case 01
    def test_case_1_verify_all_products_and_product_detail_page(self): 
        self.browser.get("http://159.223.80.88:9873/kelontong-store/products")
        time.sleep(2)

        actions = ActionChains(self.browser)
    
        hasNextPage=True
        nextpage=2
        while(hasNextPage):
            page = self.browser.find_element(By.LINK_TEXT, str(nextpage))
            actions.move_to_element(page)
            actions.click(page)
            actions.perform()
            time.sleep(2) 
            nextpage=nextpage+1

            if not self.browser.find_elements(By.LINK_TEXT, str(nextpage)):
                hasNextPage=False

    @classmethod 
    def tearDownClass(cls): # tutup browser
        cls.browser.close() 

if __name__ == "__main__": 
    unittest.main()