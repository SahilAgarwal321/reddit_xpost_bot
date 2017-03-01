import config
import praw
from time import sleep


def initialise_reddit():
    '''Initialise the reddit instance'''
    reddit = praw.Reddit(user_agent=config.user_agent, client_id=config.client_id, client_secret=config.client_secret, username=config.username, password=password)
    print '>> {}'.format(config.user_agent)
    print '>> logging in as {}'.format(config.username)
    return reddit


# def initialise_subreddits(reddit):
    # '''Initialise the subreddits instance'''
    # subreddits = get_subreddits()
    # subreddits = reddit.subreddit(subreddits)
    # return subreddits


def initialise_subreddit(reddit):
    '''Initialise the subreddit instance'''
    subreddit = reddit.subreddit(config.subreddit)
    return subreddit


def get_subreddits():
    '''Parses subreddits from config files in format understood by reddit API.
    Used for multiple subreddits. \n
    Example - \n
    Input from config file : ['AskReddit','NoStupidQuestions']\n
    Output : 'AskReddit+NoStupidQuestions'
    '''
    subreddits_text = ''
    for subreddit in config.subreddits:
        subreddits_text = subreddits_text + subreddit + '+'
    return subreddits[:-1]


def initialise_submissions(subreddit):
    '''Initialise the submissions stream'''
    return subreddit.stream.submissions()


def process_submissions(submissions):
    '''Process the submissions stream'''
    for submission in submissions:
        process_submission(submission)


def process_submission(submission):
    '''Process individual submission instance'''
    submission_type = get_submission_type(submission)
    if submission_type == 'self':
        process_self_submission(submission)
    else:
        process_link_submission(submission)


def get_submission_type(submission):
    '''Get submission type - self post or linked post'''
    # return submission.type
    # to do


def process_self_submission(submission):
    '''Process individual submission instance of type "self"'''
    normalized_title = submission.title.lower()
    for phrase in config.phrases:
        # edit next line to include check for phrase in content of self post
        if phrase in normalized_title:
            other_subreddits = get_other_subreddits_self_post(submission)
            # get subreddit from title or content of self post
            reply(submission, other_subreddits)
            # A reply has been made so do not attempt to match other phrases.
            break


def get_other_subreddits_self_post(submission):
    '''get links to other subreddits from title or content of self post'''
    # return ['abc', 'def']
    # to do


def process_link_submission(submission):
    '''Process individual submission instance of type "link"'''
    other_discussions = get_other_discussions(submission)
    other_subreddits = get_other_subreddits(submission)
    reply(submission, other_subreddits, other_discussions)


def get_other_discussions(submission):
    '''Get links to other discussions / submissions with same link posted'''
    # return ['abc', 'def']
    # to do


def get_other_subreddits(submission):
    '''Get links to other subreddits with same link posted'''
    # return ['abc', 'def']
    # to do


def reply(submission, subreddits, discussions=None):
    '''Reply to submission with top level comment'''
    reply_text = config.reply_template.format(discussions, subreddits)
    print('Replying to: {}'.format(submission.title))
    submission.reply(reply_text)
    sleep(config.sleep_after_commenting)


if __name__ == '__main__':
    reddit = initialise_reddit()
    subreddit = initialise_subreddit(reddit)
    submissions = initialise_submissions(subreddit)
    process_submissions(submissions)
