import pytest
from social import *

def test_remove_friendship():
    sg = SocialGraph()
    sg.populate_graph()
    sg.remove_friendship(1, 8) # remove friendship between user1 and user8
    assert 8 not in sg.friendships[1]

def test_change_user_name():
    sg = SocialGraph()
    sg.add_user("John")
    sg.change_user_name("John", "Johnny")
    assert sg.users[1].name == "Johnny"

def test_get_friends():
    sg = SocialGraph()
    sg.populate_graph()
    assert sg.get_friends(1) == {8: "Susan", 10: "Tom", 5: "Alex"}

#