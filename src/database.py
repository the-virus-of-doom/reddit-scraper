"""
Testing the database module.
"""
import os
from tinydb import TinyDB, Query
from modules import post

# create a database
db = TinyDB('data' + os.sep + 'db.json')

User = Query()

def seed_db():
    """
    Seed the database with some test data.
    """
    seed_post = post.Post()
    seed_post.init_full('11r47so', 'https://www.reddit.com/r/Animewallpaper/comments/11r47so/sunflower_original_2400x3840/', 'Sunflower [Original] (2400x3840)', False, '2020-01-01 00:00:00', 'submission', 'image', 'https://i.redd.it/giuzyu1h2pna1.png', ['test', 'custom_tag', 'custom_tag_1'])  # noqa: E501
    add_post(seed_post)
    seed_post.init_full('10wcrny', 'https://www.reddit.com/r/titanfall/comments/10wcrny/i_drew_bt/', 'I drew BT :)', False, '2020-01-01 00:00:00', 'submission', 'image', 'https://i.redd.it/qkyep9daxtga1.jpg', ['test', 'custom_tag', 'custom_tag_2'])  # noqa: E501
    add_post(seed_post)
    seed_post.init_full('rs49ne', 'https://www.reddit.com/r/Komi_san/comments/rs49ne/whos_more_worthy_of_protecting_komisan_or_bt7274/', 'Who’s more worthy of protecting Komi-san or bt-7274?', False, '2020-01-01 00:00:00', 'submission', 'text', '', ['test', 'custom_tag', 'custom_tag_3'])  # noqa: E501
    add_post(seed_post)

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
seed_db()
print(get_all_posts())
reset_db(True)
print(get_all_posts())
