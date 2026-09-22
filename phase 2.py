from collections import deque

# Graph using adjacency list
graph = {}


# Add a new user
def add_user(user):
    if user not in graph:
        graph[user] = set()
        print(user, "added successfully.")
    else:
        print(user, "already exists.")


# Add friendship between two users
def add_friendship(user1, user2):
    if user1 not in graph:
        add_user(user1)

    if user2 not in graph:
        add_user(user2)

    graph[user1].add(user2)
    graph[user2].add(user1)

    print("Friendship created between", user1, "and", user2)


# Find mutual friends
def mutual_friends(user1, user2):
    if user1 not in graph or user2 not in graph:
        return set()

    return graph[user1].intersection(graph[user2])


# Recommend friends
def recommend_friends(user):
    if user not in graph:
        print("User not found.")
        return

    direct_friends = graph[user]
    recommendations = {}

    # Check friends of direct friends
    for friend in direct_friends:
        for candidate in graph[friend]:

            # Ignore the user and existing friends
            if candidate == user or candidate in direct_friends:
                continue

            # Count mutual friends
            count = len(graph[user].intersection(graph[candidate]))

            recommendations[candidate] = count

    # Sort by mutual friend count
    sorted_recommendations = sorted(
        recommendations.items(),
        key=lambda x: x[1],
        reverse=True
    )

    print("\nFriend Recommendations for", user)

    if not sorted_recommendations:
        print("No recommendations found.")
    else:
        for candidate, count in sorted_recommendations:
            print(candidate, "->", count, "mutual friend(s)")


# BFS Traversal
def bfs(start):
    if start not in graph:
        print("User not found.")
        return

    visited = set()
    queue = deque([start])

    print("\nBFS Traversal:")

    while queue:
        current = queue.popleft()

        if current not in visited:
            print(current, end=" ")
            visited.add(current)

            for friend in graph[current]:
                if friend not in visited:
                    queue.append(friend)

    print()


# -----------------------------
# Main Program
# -----------------------------

# Add users
users = ["A", "B", "C", "D", "E", "F"]

for user in users:
    add_user(user)

# Create friendships
add_friendship("A", "B")
add_friendship("A", "C")
add_friendship("B", "D")
add_friendship("B", "E")
add_friendship("C", "F")

# Display graph
print("\nSocial Network:")
for user in graph:
    print(user, "->", graph[user])

# Friend recommendations
recommend_friends("A")

# BFS traversal
bfs("A")v 