from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ContactsDB.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Contact(db.Model):
    contact_id = db.Column(db.Integer, primary_key=True)
    contact_name = db.Column(db.String(255), nullable=False)
    contact_phone = db.Column(db.String(255), nullable=False)
    contact_email = db.Column(db.String(255))
    contact_address = db.Column(db.String(255))

    def __repr__(self):
        return f"Contact: {self.contact_id}"


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        current_name = request.form["contact-name"]
        current_phone = request.form["contact-phone"]
        current_email = request.form["contact-email"]
        current_address = request.form["contact-address"]
        new_contact = Contact(contact_name=current_name, contact_phone=current_phone,
                              contact_email=current_email, contact_address=current_address)
        try:
            db.session.add(new_contact)
            db.session.commit()
            return redirect("/")
        except Exception as e:
            return f"Operation failed: {e}"
    else:
        contacts = Contact.query.all()
        return render_template("index.html", contacts=contacts)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
