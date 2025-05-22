# Flask Contact Form Web App

This is a simple Flask-based web application that provides a contact form allowing users to submit their name, email, and message. Submissions are stored in a SQLite database, and confirmation emails are sent to both the user and an admin using SendGrid.

##  Features

- Contact form for user input
- Stores form submissions in a SQLite database
- Sends confirmation email to the user
- Sends notification email to the admin
- Basic success page upon form submission

## Project Structure

├── app.py
├── contact.db # Created automatically on first run
├── templates/
│ ├── contact.html
│ └── success.html
├── requirements.txt
└── README.md


## 🛠️ Technologies Used

- Python 3.x
- Flask
- SQLite
- SendGrid (for email delivery)
- HTML (Jinja2 templates)

## 📝 Prerequisites

- Python 3.x
- A SendGrid account with an API key

## 🔧 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/ameerhamza6813/Task-11.git
   cd flask-contact-form

## Create Environment and install Dependencies

BASH

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install flask sendgrid

## Run the app

bash
python app.py

Access the app
Open your browser and go to http://localhost:5000