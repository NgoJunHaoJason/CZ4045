import praw
import pandas as pd
import datetime as dt
from slugify import slugify

reddit = praw.Reddit(client_id='', 
                     client_secret='', 
                     user_agent='r-python-scrapper-1', 
                     username='r-python-scrapper', 
                     password='')


subreddit = reddit.subreddit('python')
top_subreddit = subreddit.top(limit=20)


for submission in top_subreddit:
    file_name = 'r-python/'+slugify(submission.title)+'.txt'
    with open(file_name, 'wb') as txt_file:
        txt_file.write((submission.selftext+'\n').encode('utf8'))
    txt_file.close()
    
    for top_level_comment in submission.comments:
            if top_level_comment.body!='[deleted]':
                with open(file_name, 'ab') as txt_file:
                    txt_file.write((top_level_comment.body+'\n').encode('utf8'))
                txt_file.close()








