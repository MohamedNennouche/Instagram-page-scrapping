# Import of used modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from instascrape import Profile, scrape_posts
from selenium.webdriver import Chrome

# Declaration of a webdriver (for me it's a Chrome webdriver)
driver = Chrome()

'''
Add here : 
- Your session ID to line 16
- Your user agent to line 18
- The username of the instagram page you want to scrape to line 21
'''
sessionID = input('Enter your session ID')
userAgent = input('Enter your user agent')
SESSIONID = sessionID
headers = {"user-agent": userAgent,
           "cookie": f"sessionid={SESSIONID};"}

instaPage = Profile("InstagramID")
instaPage.scrape(headers=headers)
posts = instaPage.get_posts(webdriver=driver, login_first=True)
scraped, unscraped = scrape_posts(posts, silent=False, headers=headers, pause=5) 

data_post = [post.to_dict() for post in scraped]
posts_df = pd.DataFrame(data_post)


# Before saving the file you can delete the columns you consider superfluous
posts_df.to_csv('post_data.csv')