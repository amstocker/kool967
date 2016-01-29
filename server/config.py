from authomatic.providers import oauth2


def load_facebook_app_info():
    import json
    with open('/usr/local/etc/fb.json') as f:
        info = json.loads(f.read())
        return info['apps']['kool967']

fb_info = load_facebook_app_info()


auth = {
    'facebook': {
        'class_': oauth2.Facebook,
        'consumer_key': fb_info["APP_ID"],
        'consumer_secret': fb_info["APP_SECRET"],
        'scope': ['public_profile']
    }
}
