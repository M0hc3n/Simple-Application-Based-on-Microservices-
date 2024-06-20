from flask import flash, redirect, url_for

import os

def process_request(request):
    if request.form["submit"] == "Test":
        ret = os.system("ping sender-service -w 1")

        if ret == 0:
            flash("The test was successfull", "green")
            return redirect(url_for("test"))
        else:
            flash("The test was failed", "red")
    elif request.form['submit_button'] == 'Reset':
            return redirect(url_for("index"))
    else:
        pass

