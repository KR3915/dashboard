from flask import Flask
app = Flask(__name__)

@app.route("/")
def show_text():
           return "<p>cego</p>"

if __name__ == '__main__':
    app.run(debug=True, port=3000)
