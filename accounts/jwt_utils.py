import time


def blacklist_key(token):
    return f"jwt:blacklist:{token}"

def get_ttl(token):
    exp = int(token["exp"])
    now = int(time.time())
    return max(exp - now, 0)