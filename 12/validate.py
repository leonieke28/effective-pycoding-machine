from collections import namedtuple

User = namedtuple("User", "name role expired")
USER, ADMIN = "user", "admin"
SECRET = "I am a very secret token"

julian = User(name="Julian", role=USER, expired=False)
bob = User(name="Bob", role=USER, expired=True)
pybites = User(name="PyBites", role=ADMIN, expired=False)
USERS = (julian, bob, pybites)


# define exception classes here
class UserDoesNotExist(Exception):
    pass


class UserAccessExpired(Exception):
    pass


class UserNoPermission(Exception):
    pass


def get_secret_token(username):
    # Check if user exists
    user = next((user for user in USERS if user.name == username), None)
    if not user:
        raise UserDoesNotExist

    # Check if user access has expired
    if user.expired:
        raise UserAccessExpired

    # Check if user is an admin
    if user.role != ADMIN:
        raise UserNoPermission

    # If all checks pass, return the secret
    return SECRET
