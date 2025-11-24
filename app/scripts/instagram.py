import requests
import re
def get_ig_followers(url='https://www.instagram.com/fent_abuser/'):
    r = requests.get(url)
    return get_follow_stats(r.text)[0]

def get_ig_following(url='https://www.instagram.com/fent_abuser/'):
    r = requests.get(url)
    return get_follow_stats(r.text)[1]

def get_follow_stats(html: str):
    pattern = r"(\d+)\s+Followers,\s+(\d+)\s+Following"
    match = re.search(pattern, html)
    if match:
        followers = int(match.group(1))
        following = int(match.group(2))
        return followers, following
    return None, None

