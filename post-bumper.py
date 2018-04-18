# BEFORE USE:
## WINDOWS: OPEN CMD AS ADMIN, NAVIGATE TO PYTHON SCRIPTS FOLDER WHERE YOUR PIP IS AND TYPE pip install praw
## LINUX-BASED: OPEN TERMINAL, TYPE pip install praw
### MAKE A NEW REDDIT ACCOUNT AND MAKE A REDDIT APP: https://www.reddit.com/prefs/apps

# TO USE THIS BOT YOU MUST SET CRON TO EACH ? OF HOURS YOU WANT THE POST TO BE BUMPED AT
# https://crontab.guru/
# YOU CAN ALSO EXECUTE THE .EXE EVERY ? HOURS MANUALLY

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
