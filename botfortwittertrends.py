from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import tweepy
import random
import openai


# Path to your webdriver. Download it from https://www.selenium.dev/documentation/en/webdriver/driver_requirements/
# Make sure to put the correct path here
options = webdriver.ChromeOptions()

# Twitter credentials
username = "your_twitter_username"
password = "your_twitter_password"

# Start a new instance of Chrome WebDriver
driver = webdriver.Chrome(options=options)

# Open Twitter login page
driver.get("https://twitter.com/i/flow/login")

# Wait for page to load
time.sleep(10)

#if driver.title == "X. It’s what’s happening / X":

try:
        
    # signin = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a/div/span/span")
    # signin.click()
    # time.sleep(2)




    # username=driver.find_element(By.CSS_SELECTOR,".r-13f91hp")
    username=driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
    username.click()
    username.send_keys('@KerySystems')
    username.send_keys(Keys.RETURN) 

    time.sleep (5)

    mypassword = driver.find_element(By.NAME, "password")
    mypassword.send_keys("@Kenya2024")
    mypassword.send_keys(Keys.RETURN)

    time.sleep(5)

    driver.get("https://twitter.com/i/trends")
    driver.refresh()

    time.sleep(20)

except:
    pass


myjokes = [
    "Why don't scientists trust atoms? Because they make up everything! ⚛️😄 #ScienceHumor #ChemistryJokes",
    "I told my computer I needed a break, and it froze. Guess it really took it to heart! 💻❄️ #TechHumor #ComputerJokes",
    "Why did the smartphone go to therapy? It had too many hang-ups! 📱🛋️ #SmartphoneHumor #TechJokes",
    "What do you call fake spaghetti? An impasta! 🍝😆 #FoodHumor #PastaJokes",
    "Why don't skeletons fight each other? They don't have the guts! ☠️😂 #SkeletonHumor #HalloweenJokes",
    "Why did the scarecrow win an award? Because he was outstanding in his field! 🌾🏆 #FarmHumor #ScarecrowJokes",
    "What did the ocean say to the shore? Nothing, it just waved! 🌊👋 #OceanHumor #BeachJokes",
    "Why don't eggs tell jokes? Because they might crack up! 🥚😄 #EggHumor #BreakfastJokes",
    "What did one hat say to the other? You stay here, I'll go on ahead! 🎩👒 #HatHumor #FashionJokes",
    "Why did the math book look sad? Because it had too many problems! 📚➕➖ #MathHumor #BookJokes"
]

trending_topics = []
# trends_container = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[4]')
# trends = trends_container.find_elements(By.CLASS_NAME, 'r-18u37iz') //working fine

trends_container = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]')
trends = trends_container.find_elements(By.CSS_SELECTOR, '.r-1bymd8e') 

for trend in trends:
    trending_topics.append(trend.text+',')


print("Trending Topics:")
n=1
for topic in trending_topics:

    print(n,':',topic)
    n=n+1


    
consumer_key = "4XLkTnyCHdkXi4jyLAp187re5"
consumer_secret = "OJeP0mcUI9IqzmsuQWdrNemgSnRLCCsB8weBWbiH5VsOJuomaf"
access_token = "1442225739818934273-bucajZTurvT4xeGFHzYm4sFol6cuQ1"
access_token_secret = "8QzGPUEdWqbTToKmQ0XqzoxsVshLBGrZ0FNzmwNC53E4x"
Bearer_token =r"AAAAAAAAAAAAAAAAAAAAAHMPswEAAAAAOdbH0bZtWnFjN707eenpb7t6n30%3DZF7GmCrvq3u0W4BFSqstSR8JYbgWCDGZKu3DpVGwdMlAw6ZZku"
# Authenticate to Twitter
search_url = "https://api.twitter.com/2/tweets/counts/recent"
client = tweepy.Client(Bearer_token,consumer_key, consumer_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

AITweets = []

def mytweepy():

    mainj=random.choice(myjokes)

    joke = random.choice(trending_topics)
    joke2 = random.sample(trending_topics,5)


    try:
        ttpcs = ' '.join(joke2)
        
        #client.create_tweet(text= joke)
        client.create_tweet(text=mainj+'\n'+ttpcs)
            
        print("Tweeted: ")
    except tweepy.TweepyException as e:
            print("Error: ", e)


mytweepy()