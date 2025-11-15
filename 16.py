class Comment:
    def __init__(self, content, author):
        self.content = content
        self.author = author
    
    def __str__(self):
        return f"{self.author.name}: {self.content}"


class Post:
    def __init__(self, content, author):
        self.content = content
        self.author = author
        self.comments = []
        self.likes = set()

    def add_comment(self, comment):
        self.comments.append(comment)

    def add_like(self, user):
        self.likes.add(user)

    def __str__(self):
        return f"{self.author.name}-is posti : {self.content}"


class User:
    def __init__(self, name):
        self.name = name
        self.posts = []
        self.friends = set()

    def add_friend(self, user):
        self.friends.add(user)
        user.friends.add(self)

    def create_post(self, content):
        post = Post(content, self)
        self.posts.append(post)
        return post

    def comment_post(self, post, content):
        comment = Comment(content, self)
        post.add_comment(comment)
        return comment

    def like_post(self, post):
        post.add_like(self)


# ahevqmnat ori momxmarebeli
user1 = User("User1")
user2 = User("User2")

# davamegobrot
user1.add_friend(user2)

# User1 qmnis posts
post1 = user1.create_post("pirveli posti.")

# User2 akomentarebs am posts
comment1 = user2.comment_post(post1, "saintereso postia")

# User1 alaikebs komentars
comment1.likes = set()
comment1.likes.add(user1)

# iqmneba meore posti
post2 = user1.create_post("meore posti")

# User2 alaikebs meore posts
user2.like_post(post2)