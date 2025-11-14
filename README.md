# Contact Book — Flask Web App

A simple yet functional **Flask-based Contact Management App** that allows users to **create, view, edit, delete, search, and export contacts** to a CSV file.  
Built with **Python, Flask, SQLAlchemy**, and **SCSS** for clean backend logic and elegant UI styling.

## Features

- Add new contacts with name, phone number, and email  
- Search contacts by name or phone number  
- Edit or delete existing contacts  
- Export all contacts to a CSV file (downloads directly)  
- Styled with SCSS (compiled using Flask-Assets + libsass)  
- Data stored locally in an SQLite database

## Installation & Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/KaramiZahra/Contact-Book
   cd Contact-Book
   ```

2. **Create a virtual environment**

   ```bash
   python3 -m venv env
   source env/bin/activate   # macOS/Linux
   env\Scripts\activate      # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**

   ```bash
   python3 app.py
   ```

Then open your browser and go to **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)** 

## Project Structure

```
Contact-Book/
│
├── app.py                     # Main Flask app
├── requirements.txt           # Dependencies
├── instance/
│   └── ContactsDB.db          # SQLite database
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── contacts.html
│   └── edit.html
├── static/
│   └── scss/
        ├── style.css
        ├── style.css.map
│       └── style.scss         # Main SCSS file
├── .gitignore
└── README.md
```

## Routes Overview

| Route          | Method     | Description                     |
| -------------- | ---------- | ------------------------------- |
| `/`            | GET / POST | Add a new contact or show form  |
| `/contacts`    | GET / POST | View all contacts or search     |
| `/edit/<id>`   | GET / POST | Edit an existing contact        |
| `/delete/<id>` | GET        | Delete a contact                |
| `/export`      | GET        | Export contacts as a CSV file   |

## Tech Stack

| Layer | Technology |
|-------|-------------|
| **Backend** | Flask (Python) |
| **Database** | SQLite (SQLAlchemy ORM) |
| **Frontend** | HTML, SCSS |
| **Styling Tools** | Flask-Assets, libsass |
| **Other** | CSV Export via `send_file()` |