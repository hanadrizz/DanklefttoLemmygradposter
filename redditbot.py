import urllib.request
import praw
import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select


driver = webdriver.Firefox()
driver.get("https://lemmygrad.ml/login")

time.sleep(3)
loginid = driver.find_element_by_id("login-email-or-username")
passwordid = driver.find_element_by_id("login-password")
loginid.send_keys("hana")
passwordid.send_keys("secret")
loginn =  driver.find_element_by_css_selector("button[class*='btn btn-secondary']")
loginn.click()



reddit = praw.Reddit(client_id="secret",
                     client_secret="secret",
                     user_agent="secret")
subreddit = reddit.subreddit(display_name="DankLeft")

# Iterate through top submissions
for submission in subreddit.top(limit=250):

    # Get the link of the submission
    url = str(submission.url)
    # Check if the link is an image
    if url.endswith("jpg") or url.endswith("jpeg") or url.endswith("png"):

        # Retrieve the image and post it
        driver.get("https://lemmygrad.ml/create_post?community_id=1347")
        options.addArguments("--disable-notifications")
        inputid = driver.find_element_by_id("post-url")
        title = driver.find_element_by_id("post-title")
        button = driver.find_element_by_css_selector("button[class*='btn btn-secondary mr-2']")
        filename = str(submission.url)
        postname = str(submission.title)
        inputid.send_keys(filename)
        title.send_keys(postname)
        button.click()
