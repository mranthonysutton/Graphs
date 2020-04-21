import random
from util import Queue


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

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users -> num_users times

        # Create friendships
        for i in range(0, num_users):
            self.add_user(f"User {i + 1}")

        # Generate all friendship combinations
        possible_friendships = []

        # Avoid duplicates by making sure first num is smaller than second num
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        # Shuffle all possible friendships
        random.shuffle(possible_friendships)

        # Create for first X pair x is total // 2
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set

        """
        # Create a queue for BFS
        queue = Queue()
        queue.enqueue([user_id])

        # While items are in the queue
        while queue.size() > 0:
            path = queue.dequeue()

            if not visited.get(path[-1], None):
                visited[path[-1]] = path

                for friend in self.friendships[path[-1]]:
                    friend_path = list(path)
                    friend_path.append(friend)
                    queue.enqueue(friend_path)

        return visited
        """

        # Shortest path lets us know that we want to do a BFS
        # Extended network lets us know we want to use a traversal on a connected component

        # How are we going to build a graph?
        # Start at a given user_id -> BFS -> return the path to each friend

        # Create queue & enqueue the path
        queue = Queue()
        queue.enqueue([user_id])

        # Add to the visited queue while queue is not empty
        while queue.size() > 0:
            # dequeue the first path
            path = queue.dequeue()

            last_item = path[-1]

            # if not visited -> add to visited
            if last_item not in visited:
                visited[last_item] = path

                # for each friend -> add the friend (neighbor) -> copy path & enqueue
                for neighbor in self.friendships[last_item]:
                    new_path = path.copy()
                    new_path.append(neighbor)
                    queue.enqueue(new_path)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(1000, 1)
    # print("FRIENDSHIPS")
    # print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    # print("CONNECTIONS")
    # print(connections)

    total_social_paths = 0
    for user_id in connections:
        total_social_paths += len(connections[user_id])

    print(
        f"Average length of social path is {total_social_paths / len(connections)}")
