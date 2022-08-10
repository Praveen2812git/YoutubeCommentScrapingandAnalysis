
## Imports

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import exceptions
import time
import io
import pandas as pd
import numpy as np
import csv
import sys
import os  # For cloud

## function definition

def scrapfyt(url):

  ## Opening chrome and url

  option = webdriver.ChromeOptions()
  option.binary_location = os.environ.get("GOOGLE_CHROME_BIN")  # For cloud
  option.add_argument('--headless')
  option.add_argument('-no-sandbox')
#   option.add_argument("--disable-infobars")
#   option.add_argument("--disable-gpu")
  option.add_argument("--mute-audio")
  option.add_argument("--disable-extensions")
  option.add_argument('-disable-dev-shm-usage')

  # driver = webdriver.Chrome(service=Service("C:/chrome extension/chromedriver.exe"), options=option) # For testing in windows

  driver = webdriver.Chrome(service = Service(executable_path = os.environ.get("CHROMEDRIVER_PATH")), options = option)  # For cloud

  driver.set_window_size(960, 800)      # minimizing window to optimum because of youtube design of
                                        # right side videos recommendations. When in max window,
                                        # while scrolling comments, it cannot be able to load correctly
                                        # due to the video recommendations in the right side.
  time.sleep(1)
  driver.get(url)
  time.sleep(2)

  ## Pause youtube video

  pause = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'ytp-play-button')))

  pause.click()
  time.sleep(0.2)
  pause.click()
  time.sleep(4)

  ## Scrolling through all the comments

  # Initial Scroll
  driver.execute_script("window.scrollBy(0,500)","")
    
  last_height = driver.execute_script("return document.documentElement.scrollHeight")

  while True:
    # Scroll down till "next load".
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")

    # Wait to load everything thus far.
    time.sleep(4)
    
    # Calculate new scroll height and compare with last scroll height.
    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    if new_height == last_height:
      break
    last_height = new_height
    
  # One last scroll just in case
  driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")

  ## Scraping details

  ## title of video
  video_title = driver.find_element(By.NAME, 'title').get_attribute('content')

  ## owner of video
  video_owner1 = driver.find_elements(By.XPATH, '//*[@id="text"]/a')
  video_owner = []
  for owner in video_owner1:
    video_owner.append(owner.text)
  video_owner = video_owner[0]

  # total comments with replies
  video_comment_with_replies = driver.find_element(By.XPATH, '//*[@id="count"]/yt-formatted-string/span[1]').text + ' Comments'

  ## Scraping all the comments
  users = driver.find_elements(By.XPATH, '//*[@id="author-text"]/span')
  comments = driver.find_elements(By.XPATH, '//*[@id="content-text"]')

  with io.open('comments.csv', 'w', newline='', encoding="utf-16") as file:
      writer = csv.writer(file, delimiter =",", quoting=csv.QUOTE_ALL)
      writer.writerow(["Username", "Comment"])
      for username, comment in zip(users, comments):
          writer.writerow([username.text, comment.text])
    
  commentsfile = pd.read_csv("comments.csv", encoding ="utf-16")  # , encoding ="utf-16", engine = 'python'

  all_comments = commentsfile.replace(np.nan, '-', regex = True)
  all_comments = all_comments.to_csv("Full Comments.csv", index = False)
  # comments.to_html("Comments2.html")

  ##total comments without replies
  video_comment_without_replies = str(len(commentsfile.axes[0])) + ' Comments'

  # print(video_title, video_owner, video_comment_with_replies, video_comment_without_replies)

  ## Close driver

  driver.close()

  # print("Scraping is finished")

  ## return fuction

  return all_comments, video_title, video_owner, video_comment_with_replies, video_comment_without_replies
