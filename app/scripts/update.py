import github_stats as gh
import instagram as ig
import time
import gmail_stats as em

def update_stats():
    stars = gh.get_stars()
    followers = gh.get_github_followers()
    ig_followers = ig.get_ig_followers()
    ig_following = ig.get_ig_following()
    gmail_sent = em.get_email1()

    from database import update_github_stats, update_instagram_stats, update_gmail_stats
    update_github_stats(stars, followers)
    update_instagram_stats(ig_followers, ig_following)
    update_gmail_stats(gmail_sent)
if __name__ == "__main__":
    while True:
        update_stats()
        time.sleep(3600)  # Update every hour