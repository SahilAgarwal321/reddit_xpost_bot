"""
Configuration file for the bot.
"""
client_id = 'CLIENT_ID'
client_secret = "CLIENT_SECRET"
password = ''
user_agent = '<platform>:<app ID>:<v1.0> (by /u/username)'
username = ''
message = '''x-post / crosspost bot. \n
Tells which subreddits submission has been crossposted to.'''

sleep_after_commenting = 2
# Seconds to sleep after commenting

subreddit = ''
# subreddits = ['abc','def']
# Subreddits the bot works on

phrases = ['xpost', 'xposted', 'x-post', 'x-posted', 'x post', 'x posted', 'crosspost', 'crossposted', 'cross-post', 'cross-posted', 'cross post', 'cross posted']
# phrases to identify submission as a crosspost

reply_template = '''For mobile users : xpost subreddit links -\n'''
