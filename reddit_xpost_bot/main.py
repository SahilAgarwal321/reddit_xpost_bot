import praw
import config


def initialise_reddit():
    reddit = praw.Reddit(user_agent=config.user_agent, username=config.username, password=password, client_id=config.client_id, client_secret=config.client_secret)
    reddit.
    print '>> logging in as {}'.format(config.username)
