import pytest
from social import *

def test_remove_friendship():
    sg = SocialGraph()
    sg.populate_graph()
    sg.remove_friendship(1, 8) # remove friendship between user1 and user8
    assert 8 not in sg.friendships[1]

def test_create_new_social_path():
    pass
