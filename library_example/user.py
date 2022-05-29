from book import Book


class User:
    # TODO
    def __init__(self, username, password):
        self.username = username
        self.password = password


class RegularUser(User):
    # TODO
    def __init__(self, username, password):
        super().__init__(username, password)
        regular = 0
        with open('library_example/id_counter.txt', 'r') as file:
            counter = []
            for id in file.readlines():
                counter.append(id.strip("\n").split(":"))
            user_id = int(counter[0][1]) + 1
        with open('library_example/users.txt', 'a') as file, open('library_example/id_counter.txt', 'w') as file2:
            file.write(f"{user_id}:{username}:{password}:{regular}\n")
            file2.write(f"user_id:{user_id}:book_id:{counter[0][3]}")
        print(f"User {username} created with id {user_id}")


class AdminUser(User):
    # TODO
    def __init__(self, username, password):
        super().__init__(username, password)
        admin = 1
        with open('library_example/id_counter.txt', 'r') as file:
            counter = []
            for id in file.read():
                counter.append(id.strip("\n").split(":"))
            user_id = int(counter[0][1]) + 1
        with open('library_example/users.txt', 'a') as file, open('library_example/id_counter.txt', 'w') as file2:
            file.write(f"{user_id}:{username}:{password}:{admin}\n")
            file2.write(f"user_id:{user_id}:book_id:{counter[0][3]}")
        print(f"Admin {username} created with id {user_id}")
