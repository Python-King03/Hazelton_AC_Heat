from flask import Flask, render_template, request, redirect, url_for
from ses_mailer import send_lead_email
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
    if (request.form.get("bot_field") or "").strip():
        return redirect(url_for("contact_get")

    fname = request.form.get("fname", "").strip()
    lname = request.form.get("lname", "").strip()
    email = request.form.get("email", "").strip()
    phone = request.form.get("phone", "").strip()
    message = request.form.get("message", "").strip()

    # Basic validation
    if not fname or not lname or not email or not message:
        return "Invalid submission", 400

    subject = f"New website lead: {fname} {lname}"
    body = (
        f"Name: {fname} {lname}\n",
        f"Email: {email}\n",
        f"Phone: {phone}\n\n",
        f"Message:\n{message}\n",
    )

    send_lead_email(subject=subject, body=body, reply_to=email)

    return redirect(url_for("contact_get"))

@app.get("/")
def index():
    if (y := datetime.datetime.now().year) != 2025:
        return render_template("index.html",year=f"2025-{y}")
    else:
        return render_template("index.html",year="2025")

