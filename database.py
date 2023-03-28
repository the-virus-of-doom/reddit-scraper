"""
Testing the database module.
"""
import os
from tinydb import TinyDB, Query
from modules import post

# create a database
db = TinyDB('data' + os.sep + 'db.json')

User = Query()

def seed_db_with_posts():
    """
    Seed the database with some test data.
    """
    seed_post = post.Post('', '', 'Test Post', False, '2020-01-01 00:00:00', 'submission', 'text', 'this is some text', ['test', 'custom_tag', 'custom_tag_1'])  # noqa: E501
    add_post(seed_post)
    seed_post = post.Post('', '', 'Test Post 2', False, '2020-01-01 00:00:00', 'submission', 'text', 'this is some text', ['test', 'custom_tag', 'custom_tag_2'])  # noqa: E501
    add_post(seed_post)

def seed_db():
    """
    Seed the database with some test data.
    """
    db.insert({ 'id': '1',
                'reddit_id': '',
                'permalink_url': '' ,
                'title': 'Test Post `',
                'url': 'https://www.reddit.com/',
                'is_nsfw': False,
                'access_date': '2020-01-01 00:00:00',
                'post_type': 'submission',
                'post_content_type': 'text',
                'post_content': 'this is some text',
                'tags': [
                            'test',
                            'custom_tag',
                            'custom_tag_1',
                        ]
                })
    db.insert({ 'id': '2',
                'reddit_id': '',
                'permalink_url': '' ,
                'title': 'Test Post 2',
                'url': 'https://www.reddit.com/',
                'is_nsfw': False,
                'access_date': '2020-01-01 00:00:00',
                'post_type': 'submission',
                'post_content_type': 'text',
                'post_content': 'this is some text',
                'tags': [
                            'test',
                            'custom_tag',
                            'custom_tag_2',
                        ]
                })

def reset_db(reset = False):
    """
    Reset the database.

    Args:
        reset (bool, optional): A confirmation flag. Defaults to False.
    """
    if reset:
        db.truncate()
    else:
        raise UserWarning('Resetting the database requires a confirmation flag!')

def get_all_posts():
    """
    Get all posts from the database.
    """
    return db.all()

def add_post(new_post: post):
    """
    Add a post to the database.
    """
    db.insert(new_post.__dict__)

def get_post(reddit_id: str):
    """
    Get a post from the database.
    """
    return db.search(User.reddit_id == reddit_id)

# testing

reset_db(True)
seed_db_with_posts()
print(get_all_posts())
reset_db(True)
print(get_all_posts())
