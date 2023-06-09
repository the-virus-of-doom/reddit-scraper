"""
Main file for the Reddit Scraper Bot.
"""

import os
import praw

# check to see if the praw.ini file exists
if not os.path.isfile("praw.ini"):
    print("praw.ini file not found. Please copy the example and add your Reddit keys.")
    exit(1)

# import the praw.ini file
reddit = praw.Reddit('scraper1', config_interpolation="basic")

# testing praw

# get the 5 most recent saved posts from the user
saved_posts = reddit.user.me().saved(limit=5)

for saved_post in saved_posts:
    # check to see if the saved post is a comment
    if isinstance(saved_post, praw.models.Comment):
        print('COMMENT: \n' + saved_post.body)
    # check to see if the saved post is a submission
    elif isinstance(saved_post, praw.models.Submission):
        print('SUBMISSION: \n' + saved_post.title)
