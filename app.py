from flask import Flask, render_template, request
from model import recommend_destination

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        user_type = request.form["type"]
        user_budget = request.form["budget"]
        user_season = request.form["season"]

        result = recommend_destination(
            user_type,
            user_budget,
            user_season
        )

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)