import praw
import re
import time

reddit = praw.Reddit(client_id='id',
                     client_secret='secid',
                     user_agent='<platform:name:version (by username)>',
                     username='username',
                     password='password')

subreddits = ['test']
# subreddits = ['SUB1', 'SUB2', 'SUB3'] - USE THIS CODE FOR MULTI-POST
pos = 0
errors = 0

title = "Code uploaded by /r/4ZUR4, original by DrRoach"
url = "https://www.youtube.com/watch?v=ujflrixMl8I"

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
