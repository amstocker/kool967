import os


def generate_oauth_secret():
    """
    Generates 20 random bytes.
    """
    return os.urandom(20)
