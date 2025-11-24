from flask import Flask
import scripts.github as gh
from flask import render_template
import scripts.instagram as ig
app = Flask(__name__)

@app.route("/")
def show_text():
           return render_template("dashboard/dashboard.html", 
                                  github_stars=gh.get_stars(), 
                                  github_followers=gh.get_github_followers(),
                                  ig_followers=ig.get_ig_followers(),
                                  ig_following=ig.get_ig_following())




if __name__ == '__main__':
    app.run(debug=True, port=3000)
