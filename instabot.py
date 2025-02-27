from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import random

class InstaPy():
    
    def __init__(self):
        self.browser = webdriver.Firefox()
        time.sleep(0.5)
        
    def login(self):
        self.login = "Seovileo"
        self.password = "Firekon1@"
        time.sleep(8)
        self.browser.get('https://www.instagram.com/')
        time.sleep(3)
        #---> click to accept cookies.    
        self.acceptbutton = self.browser.find_element(By.XPATH, '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]')
        time.sleep(6)
        self.acceptbutton.click()
        time.sleep(6)
        ##---> end    
        self.emailForm = self.browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
        self.emailForm.click()
        self.emailForm.send_keys(self.login)
        time.sleep(3)
        self.passwordForm = self.browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')
        self.passwordForm.click()
        self.passwordForm.send_keys(self.password)
        time.sleep(1)
        self.loginButton = self.browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]')
        time.sleep(1)
        self.loginButton.click()
        time.sleep(15)


    ### ---> add_hashtags_and_search
    ### Function is responsible for open and run browser with random hashtag form hashtags[]
    def add_hashtags_and_search(self):   
        
        self.hashtags = ['wroclaw','warszawa','biznes','firma','strona','stronainternetowa','stronawww']
        self.liczba = len(self.hashtags)
        self.hashtags_rand = random.randint(0, self.liczba -1)
        time.sleep(4)
        self.browser.get('https://www.instagram.com/explore/tags/' + self.hashtags[self.hashtags_rand] + '/' )
        time.sleep(3)
        self.rand = random.randint(1000,3000)
        self.rand = str(self.rand)
        self.browser.refresh()
        time.sleep(5)
        self.browser.execute_script("window.scrollTo(10," + self.rand + ")")
        print('current #', self.hashtags[self.hashtags_rand])
        time.sleep(3)
    
    ### ---> open_photo
    ### Function is responsible for open random picture on website.     
    def open_photo(self): 
        
        self.left = random.randint(1,3)
        self.left = str(self.left)
        self.downIndex = random.randint(1,3)
        self.downIndex = str(self.downIndex)
        print('self.left', self.left)
        print('self.downIndex', self.downIndex)
        self.photo = self.browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/article/div/div/div/div['+ self.left + ']/div['+ self.downIndex +']/a/div')
        self.photo.click()
        time.sleep(2)
        
    ### ---> skip_photo
    ### Function is responsible for random skipp to next photo.    
    def skip_photo(self):
        time.sleep(2)
        
        self.skip_photo_button = self.browser.find_element(By.XPATH, '/html/body/div[7]/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]')
        self.logic_skip_photo = random.randint(1,3)
        self.i = 0
        while self.i < self.logic_skip_photo:
            time.sleep(1.5)
            self.skip_photo_button = self.browser.find_element(By.XPATH, '/html/body/div[7]/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]')
            time.sleep(1)
            self.skip_photo_button.click()
            self.i = self.i + 1
            print('skip {} photo, {}'.format(self.logic_skip_photo, self.i))    
            
     
    ### ---> like_photo_or_get_info
    ### Function is responsible for get user name and like photo.   
    def like_photo_or_get_info(self):
        
        time.sleep(0.5)
        self.like_button = self.browser.find_element(By.XPATH, '/html/body/div[7]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/div')
        time.sleep(0.5)
        
        self.like_button.click()    
        
        
    ### ---> next_photo
    ### Function is responsible for click to next photo.  
    def next_photo(self):
        time.sleep(2)
        self.next_photo_button = self.browser.find_element(By.CLASS_NAME, '_abl-')
        time.sleep(2)
        self.next_photo_button.click()
     
        
    ### ---> relax
    ### Function is responsible for pause.   
    def relax(self):
        
        self.relax_time = random.randint(505,999)
        print('InstaBotPy has stopped at this moment. The system will boot up in ', self.relax_time, ' seconds')
        time.sleep(self.relax_time)
        
    ### ---> change hash
    ### Function is responsible change hash.     
    def change_hash(self):
        
        self.hashtags_rand = random.randint(0, self.liczba -1)
        time.sleep(2)
        self.browser.get('https://www.instagram.com/explore/tags/' + self.hashtags[self.hashtags_rand] + '/' )
        print('# changed to # ' + self.hashtags[self.hashtags_rand])
        time.sleep(5)
    
    def random_like(self):
        
        self.amount = random.randint(49,79) # ammount like for # sesion.
        print('quantity like at this session - ', self.amount)
        
        
    ### ---> auto_like
    ### Function is responsible for auto like photo. 
    def auto_like(self):
        
        self.random_like()
        p_liked = 0
        while True:
            
          if p_liked == self.amount: # liczba przejsc petli:
              self.change_hash() 
              p_liked = 0
              self.relax()
              self.browser.refresh()
              time.sleep(7)
              try:
                  self.open_photo()
              except Exception:     
                  self.open_photo()
              time.sleep(4)
              self.skip_photo()
          else:
            time.sleep(5)
            try:
                self.like_photo_or_get_info()
            except Exception:     
                self.next_photo()       
            self.relax_after_like = random.randint(2,14)
            time.sleep(self.relax_after_like)
            self.next_photo()
            p_liked = p_liked + 1

bot = InstaPy()
bot.login()
bot.add_hashtags_and_search()     
bot.open_photo()   
bot.skip_photo()
bot.auto_like()
