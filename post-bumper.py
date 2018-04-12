# TO USE THIS BOT YOU MUST SET CRON TO EACH ? OF HOURS YOU WANT THE POST TO BE BUMPED AT
# https://crontab.guru/

import praw
import re

reddit = praw.Reddit(client_id='id',
                     client_secret='secid',
                     user_agent='<platform:name:version (by username)>',
                     username='username',
                     password='pw')

subreddit = reddit.subreddit('test')
for submission in subreddit.hot(limit=5):

        if re.search("TITLE KEYWORD", submission.title, re.IGNORECASE):
            submission.reply("The robots are taking over!")
            print("Bot replying to : ", submission.title)
