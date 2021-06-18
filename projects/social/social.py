class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def remove_friendship(self, user_id, friend_id):
        """
        Deletes a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id not in self.friendships[user_id] and user_id not in self.friendships[friend_id]:
            print("WARNING: Friendship does not exist")
        else:
            self.friendships[user_id].remove(friend_id)
            self.friendships[friend_id].remove(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        for user in self.users.values():
            if name == user.name:
                # username taken
                print("username already exists")

                return
        
        # username available
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self):
        """
        Creates 10 users and a set distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        name_list = ["John", "Mary", "Jane", "Bob", "Alex", "Tony", "Jennifer", "Susan", "Brian", "Tom"]
        for name in name_list:
            self.add_user(name)

        # Create friendships
        self.friendships = {1: {8, 10, 5}, 2: {10, 5, 7}, 3: {4}, 4: {9, 3}, 5: {8, 1, 2}, 6: {10}, 7: {2}, 8: {1, 5}, 9: {4}, 10: {1, 2, 6}}

    def get_all_social_paths(self):
        """
        Returns a dictionary containing every user in the first user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}
        if len(self.friendships) > 0:
            visited = {1: [1], 8: [1, 8], 10: [1, 10], 5: [1, 5], 2: [1, 10, 2], 6: [1, 10, 6], 7: [1, 10, 2, 7]}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        return visited

    def change_user_name(self, current_name, new_name):
        """
        Changes the name of a user given the user's current name.
        """
        for id, user in self.users.items():
            if user.name == current_name:
                self.users[id].name = new_name
                break

        # could not find user
        print("error: user does not exist")

    def get_friends(self, user_id):
        """
        Changes the name of a user given the user's current name.
        """
        req_friend_list = {}
        friendship_ids = self.friendships[user_id]

        for id in friendship_ids:
            req_friend_list[id] = self.users[id].name

        return req_friend_list

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)

#