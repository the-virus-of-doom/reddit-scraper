import pytest
from modules import post


def test_get_tags():
    test_post = post.Post()

    test_post.tags = []
    assert test_post.get_tags() == []
    test_post.tags = ['apple', 'banana', 'orange']
    assert test_post.get_tags() == ['apple', 'banana', 'orange']

def test_set_tags():
    test_post = post.Post()

    test_post.set_tags([])
    assert test_post.tags == []
    test_post.set_tags(['apple', 'banana', 'orange'])
    assert test_post.tags == ['apple', 'banana', 'orange']
