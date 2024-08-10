
from time import sleep
 
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common import keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from datetime import datetime


class bidder_app:
        
    PE=open("Password.txt", "r")
    EE=open("Email.txt", "r")
    

    TT=open("TemplateMessage.txt", 'r')
    Temstr=TT.read()

    
    StartOrder=open("startorder.txt", 'r')
    PATH= "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.maximize_window()
    driver.get("https://studybay.com/") 
    sleep(8)
         
    def Logger (self):
     


        try:
            signin_btn=WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.driver.find_element_by_id("login-link")) ) 
            signin_btn.click()
            # email_Input=WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.driver.find_element_by_name("email")))
            email_Input = self.driver.find_element_by_name("email")
            email_Input.click()
            estr=self.EE.read()
            email_Input.send_keys(estr)
            # email_Input.send_keys(str(self.EE))
            
            # password_Input=WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.driver.find_element_by_name("password")))
            password_Input=self.driver.find_element_by_name("password")
            password_Input.click()
            pestr=self.PE.read()
            password_Input.send_keys(pestr)
            password_Input.send_keys(Keys.ENTER)
            self.EE.close()
            self.PE.close()
        except:

            if self.driver.current_url=="https://studybay.app/home":
                pass
            if self.driver.title=="Studybay":
                pass
        

        #project_search = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[3]/div[1]/a[1]")
        #project_search.click()
    
    def Bidder (self):

        
        link="https://studybay.app/order/getoneorder/"
        SOstr=self.StartOrder.read()
        orderNo=int(SOstr)
        self.StartOrder.close()

        bids=1000000
        lastbid=orderNo+bids        
        
        for item in range (orderNo, lastbid):
            item=(link+str(orderNo))
            self.driver.get(item)
            P_Error = self.driver.title
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            try:
                if P_Error!="Error":
                    Hire_btn=WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.driver.find_element_by_css_selector(".button.green")))
                    sleep(5)
                    Hire_btn.click()
                    sleep(5)
                    
                    try:                                 
                        YesBtn=self.driver.find_element_by_css_selector(".kbyLRS")
                        if EC.visibility_of(YesBtn):
                            YesBtn.click()
                            pass                    
                    except:
                        pass 

                                             

                    Bidmsg=WebDriverWait(self.driver, 30).until(EC.visibility_of(self.driver.find_element_by_css_selector(".auctionTextarea-converted__textarea--full")))
                    Price=WebDriverWait(self.driver, 30).until(EC.visibility_of(self.driver.find_element_by_css_selector(".eerQOm")))
                    MinBid=self.driver.find_element_by_css_selector(".fnBQUJ").text
                    sleep(3)
                    Price.click()
                    Price.send_keys(MinBid)
                    Bidmsg.click()
                   
                    Bidmsg.send_keys(self.Temstr)
                    Bidmsg.send_keys(Keys.TAB, Keys.ENTER)
                    sleep(5)
                    
                    print ("BID SUCCESFUL: ", orderNo, " : ", current_time)
                    orderNo=orderNo+1
                    sleep(3)
                  
                    continue
                    
                else:
                    print (P_Error, " : ", orderNo, " : ", current_time)
                    orderNo=orderNo+1
                    continue
            except:
                if P_Error=="404 Page Not Found":
                        orderNo=orderNo
                        self.driver.refresh()                                                                                                                         
                        continue
                
                
                else:
                    orderNo=orderNo+1

              
C1=bidder_app()
C1.Logger()
C2=bidder_app()
C2.Bidder() 




