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

subreddits = ['DiscordLinks', 'discordserver', 'DiscordAdvertising', 'DiscordAppServers', 'MakeDiscordFriends']
# subreddits = ['DiscordLinks', 'discordserver', 'DiscordAdvertising']
pos = 0
errors = 0

title = "blu_ | VOICE | New community looking for active members, come check us out! Our primary game is PUBG!"
url = "https://discord.me/blu"

def post():
    global subreddits
    global pos
    global errors

    try:
        subreddit = reddit.subreddit(subreddits[pos])
        subreddit.submit(title, url=url)
        print("Posted to " + subreddits[pos])

        pos = pos + 1

        if (pos <= len(subreddits) -1):
            post()
        else:
           print("Done")
    except praw.exceptions.APIException as e:
            if (e.error_type == "RATELIMIT"):
                delay = re.search("(\d+) minutes?", e.message)
                print (e.message)
                if delay:
                    delay_seconds = float(int(delay.group(1)) * 60)
                    time.sleep(delay_seconds)
                    post()
                else:
                        delay = re.search("(\d+)", e.message)
                        delay_seconds = float(delay.group(1))
                        time.sleep(delay_seconds)
                        post()
    except:
        errors = errors + 1
        if (errors > 5):
          print("Crashed")
          exit(1)

    post()

post()
