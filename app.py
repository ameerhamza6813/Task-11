from flask import Flask, render_template, request, redirect
import sqlite3
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

app = Flask(__name__)


SENDGRID_API_KEY = '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'
ADMIN_EMAIL = 'ameer.hamza@alphabridgeconsulting.com'

def init_db():
    conn = sqlite3.connect('contact.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def send_email(to_email, subject, content):
    if not SENDGRID_API_KEY or SENDGRID_API_KEY == 'YOUR_SENDGRID_API_KEY_HERE':
        print("[ERROR] SendGrid API key is missing or placeholder is still used.")
        return

    message = Mail(
        from_email='ameer.hamza@alphabridgeconsulting.com',
        to_emails=to_email,
        subject=subject,
        plain_text_content=content
    )

    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(f"[SUCCESS] Email sent to {to_email} - Status Code: {response.status_code}")
    except Exception as e:
        print(f"[ERROR] Failed to send email to {to_email}. Exception: {e}")


@app.route('/', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        conn = sqlite3.connect('contact.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)', (name, email, message))
        conn.commit()
        conn.close()

        send_email(
            to_email=email,
            subject='Thanks for contacting us!',
            content=f"Hi {name},\n\nThank you for your message. We’ll get back to you soon!\n\nYour message:\n{message}"
        )

        send_email(
            to_email=ADMIN_EMAIL,
            subject='New Contact Form Submission',
            content=f"Name: {name}\nEmail: {email}\nMessage:\n{message}"
        )

        return redirect('/success')

    return render_template('contact.html')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
