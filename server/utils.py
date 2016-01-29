import os

SECRET_FILENAME = ".secret"


def generate_oauth_secret():
    """
    Generates 20 random bytes.
    """
    return os.urandom(20)

def load_oauth_secret():
    """
    Checks for oauth secret or else generates a new one.
    """
    if os.path.isfile(SECRET_FILENAME):
        with open(SECRET_FILENAME) as f:
            return f.read()
    else:
        secret = generate_oauth_secret()
        with open(SECRET_FILENAME, 'w') as f:
            f.write(secret)
        return secret
