from flask import Flask, render_template, request, redirect, url_for
import datetime

app = Flask(__name__)

@app.get("/contact")
def contact_get():
    if (y := datetime.datetime.now().year) != 2025:
        return render_template("contact.html",year=f"2025-{y}")
    else:
        return render_template("contact.html",year="2025")

@app.post("/contact")
def contact_post():
    fname = request.form.get("fname", "").strip()
    lname = request.form.get("lname", "").strip()
    email = request.form.get("email", "").strip()
    phone = request.form.get("phone", "").strip()
    message = request.form.get("message", "").strip()

    # Basic validation
    if not fname or not lname or not email or not message:
        return "Invalid submission", 400

    # TODO: send email (next step)
    print("CONTACT FORM SUBMISSION:")
    print(fname, lname, email, phone, message)

    return redirect(url_for("contact_get"))

@app.get("/")
def index():
    if (y := datetime.datetime.now().year) != 2025:
        return render_template("index.html",year=f"2025-{y}")
    else:
        return render_template("index.html",year="2025")

