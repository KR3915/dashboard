from flask import Flask
from flask import render_template
import scripts.instagram as ig
import scripts.get_stats as stats
import scripts.weather as wt
import scripts.welcome as welcome

temp, weather_text, weather_img, temp_feel = wt.get_weather()
print(f'Current weather in Prague: {temp}°C, {weather_text}, feels like {temp_feel}°C')
app = Flask(__name__)

@app.route("/")
def show_text():
           return render_template("dashboard/dashboard.html",
                                  welcome=welcome.get_welcome_message(),
                                  github_stars=stats.get_latest_github_stats()[0],
                                  github_followers=stats.get_latest_github_stats()[1],
                                  ig_followers=stats.get_latest_instagram_stats()[0],
                                  ig_following=stats.get_latest_instagram_stats()[1],
                                  gmail_sent=str(stats.get_latest_gmail_stats()),
                                  temp=temp,
                                  weather_description=weather_text,
                                  weather_icon=weather_img,
                                  temp_feel=temp_feel
                                  )



if __name__ == '__main__':
    temp, weather_text, weather_img, temp_feel = wt.get_weather()
    print(f'Current weather in Prague: {temp}°C, {weather_text}, feels like {temp_feel}°C')
    app.run(debug=True, port=3000)