from flask import Flask, render_template, request, flash, redirect, url_for

import requests
import os


app = Flask(__name__)
app.secret_key = "helloworld!"


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        if request.form["submit"] == "Test":
            ret = os.system("ping sender-service -w 1")

            if ret == 0:
                flash("The test was successfull", "green")
                return redirect(url_for("test"))
            else:
                flash("The test was failed", "red")
        elif request.form["submit"] == "Reset":
            return redirect(url_for("index"))
    else:
        pass

    return render_template("index.html")


@app.route("/test", methods=["POST", "GET"])
def test():
    if request.method == "POST":
        if request.form["submit"] == "Reset":
            return redirect(url_for("index"))

        elif request.form["submit"] == "What time is it ?":
            data = requests.get("http://sender-service:5051/get-time").json()
            flash(str(data["message"]), "green")
            return redirect(url_for("test"))

        elif request.form["submit"] == "Where am I ?":
            data = requests.get("http://sender-service:5051/get-location").json()
            flash(str(data["message"]), "green")
            return redirect(url_for("test"))
        else:
            pass

    return render_template("test.html")


if __name__ == "__main__":
    app.run(debug=True, port=5050, host="0.0.0.0")
