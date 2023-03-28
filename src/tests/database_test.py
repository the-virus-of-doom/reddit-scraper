import database
from modules import post

def test_seed_db():
    database.seed_db()
    assert len(database.db) == 3

def test_reset_db():
    database.seed_db()
    database.reset_db(True)
    assert len(database.db) == 0

def test_add_post():
    database.reset_db(True)
    test_post = post.Post()
    test_post.init_full('11r47so', 'https://www.reddit.com/r/Animewallpaper/comments/11r47so/sunflower_original_2400x3840/', 'Sunflower [Original] (2400x3840)', False, '2020-01-01 00:00:00', 'submission', 'image', 'https://i.redd.it/giuzyu1h2pna1.png', ['test', 'custom_tag', 'custom_tag_1'])  # noqa: E501
    database.add_post(test_post)
    assert len(database.get_all_posts()) == 1
    assert database.get_all_posts()[0]['reddit_id'] == '11r47so'

def test_get_post():
    database.reset_db(True)
    database.seed_db()
    assert len(database.get_post('11r47so')) == 1
    assert database.get_post('11r47so')[0]['reddit_id'] == '11r47so'

def test_get_all_posts():
    database.reset_db(True)
    database.seed_db()
    assert len(database.get_all_posts()) == 3
