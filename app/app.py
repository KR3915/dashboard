from flask import Flask
import scripts.github as gh
from flask import render_template
import scripts.instagram as ig
import scripts.get_stats as gs

app = Flask(__name__)

@app.route("/")
def show_text():
           return render_template("dashboard/dashboard.html", 
                                  github_stars=gs.get_latest_github_stats()[0], 
                                  github_followers=gs.get_latest_github_stats()[1],
                                  ig_followers=gs.get_latest_instagram_stats()[0],
                                  ig_following=gs.get_latest_instagram_stats()[1])




if __name__ == '__main__':
    app.run(debug=True, port=3000)
