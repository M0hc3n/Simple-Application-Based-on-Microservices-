from flask import flash, redirect, url_for

import requests

def process_test_request(request):
    if request.form["submit"] == "Reset":
        return redirect(url_for("index"))

    elif request.form["submit_button"] == "Get Message":
        data = requests.get("http://sender-service:5051").json()
        flash(str(data), "green")
        return redirect(url_for("test"))
    else:
        pass
