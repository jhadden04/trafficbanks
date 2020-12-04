import praw
import time
reddit = praw.Reddit(client_id='*',
                     client_secret='*',
                     user_agent='a reddit instance',
                     username='*',
                     password='*')

def imageposter():
    subreddits = ["gaming", "esports", "games", "gamingnews", "twitch_startup", "pcgaming"
                  "videogames", "twitch", "worldnews","news"]  # you can add to this
    n = 0
    for i in range(len(subreddits)):
        titles = ["change this"]  # you must change this to your desired title
        reddit.validate_on_submit = True
        text = ["your link"]  # you must change this to your link
        subreddit = reddit.subreddit(subreddits[n])
        try:
            subreddit.submit(titles[0], text[0])
        except:
            continue
        print(f'posted on r/{subreddit}')
        n += 1
        if n >= len(subreddits):
            n = 0
        time.sleep(900)
imageposter()
