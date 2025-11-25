import random
from telethon.tl.functions.account import CheckUsernameRequest

ADJECTIVES = ["fast", "dark", "blue", "lucky", "neo", "pure", "meta"]
NOUNS = ["fox", "lion", "bot", "node", "byte", "flow", "net"]

def generate_usernames(count=50):
    usernames = set()
    while len(usernames) < count:
        adj = random.choice(ADJECTIVES)
        noun = random.choice(NOUNS)
        suffix = random.choice(["", "x", "dev", "io", "ai", "eth"])
        username = f"{adj}{noun}{suffix}"
        if 5 <= len(username) <= 15:
            usernames.add(username)
    return list(usernames)

usernames = generate_usernames()
with open('src/utils/tg_tools/username/usernames.txt', 'w') as file:
    file.writelines(username + '\n' for username in usernames)

    