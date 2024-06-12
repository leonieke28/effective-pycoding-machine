import functools

known_users = ["bob", "julian", "mike", "carmen", "sue"]
loggedin_users = ["mike", "sue"]


def login_required(func):
    @functools.wraps(func)
    def wrapper(user):
        if user not in known_users:
            return "please create an account"
        elif user not in loggedin_users:
            return "please login"
        else:
            return func(user)

    return wrapper


@login_required
def welcome(user):
    """Return a welcome message if logged in"""
    return f"welcome back {user}"
