from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password    
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com')
        time.sleep(3)
        # bot.add_cookie({'name' : 'tour.index', 'value' : 'complete', 'domain' : self.store['base'] + url})
        email = bot.find_element_by_class_name('email-input')
        pw = bot.find_element_by_name('session[password]')
        email.clear()
        pw.clear()
        email.send_keys(self.username)
        pw.send_keys(self.password)
        pw.send_keys(Keys.RETURN)
        time.sleep(2)

    def like_tweets(self, hashtags):
        bot = self.bot
        for hashtag in hashtags:
            print('scraping hastag: ' + hashtag)
            bot.get('https://twitter.com/search?q=' + hashtag + '&src=typed_query')
            time.sleep(2)
            for i in range(1, 5):
                bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
                time.sleep(3)

            tweetLinks = [i.get_attribute('href') for i in bot.find_elements_by_xpath("//a[@dir='auto']")] # Looking for all the element where they have an attribute dir=auto - not the best way but I was in a hurry, lol
            filteredLinks = list(filter(lambda x: 'status' in x,tweetLinks)) # now once I have all the hrefs data then I can filter them out to store only the ones with the string "status" in it
            print(filteredLinks)
            for link in filteredLinks:
                bot.get(link)
                time.sleep(5)
                try:
                    bot.find_element_by_xpath("//div[@data-testid='like']").click()
                    time.sleep(15)
                except Exception as ex:
                    time.sleep(30)
            print('finished for loop')
                
            



    
tom = TwitterBot('your-mail', 'your-pw')
tom.login()
tom.like_tweets(['typescript', 'javascript', 'apollo graphql', 'serverless', 'aws'])

