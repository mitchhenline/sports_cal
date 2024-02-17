"""sport_cal application server"""

from flask import Flask, render_template
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "aggoiler"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def home():
    """app home"""

    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)