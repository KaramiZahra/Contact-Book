from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_

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
            return redirect("/contacts")
        except Exception as e:
            return f"Operation failed: {e}"

    return render_template("index.html")


@app.route("/contacts", methods=["POST", "GET"])
def show_contacts():
    if request.method == "POST":
        current_search = request.form["search"].lower().strip()
        filtered_contacts = Contact.query.filter(or_(Contact.contact_name.ilike(f"%{current_search}%"),
                                                     Contact.contact_phone.ilike(f"%{current_search}%"))).all()
        return render_template("contacts.html", contacts=filtered_contacts)
    else:
        contacts = Contact.query.all()
        return render_template("contacts.html", contacts=contacts)


@app.route("/delete/<int:id>")
def delete(id: int):
    delete_contact = Contact.query.get_or_404(id)
    try:
        db.session.delete(delete_contact)
        db.session.commit()
        return redirect("/")
    except Exception as e:
        return f"Operation failed: {e}"


@app.route("/edit/<int:id>", methods=["POST", "GET"])
def edit(id: int):
    edit_contact = Contact.query.get_or_404(id)
    if request.method == "POST":
        edit_contact.contact_name = request.form["contact-name"] or edit_contact.contact_name
        edit_contact.contact_phone = request.form["contact-phone"] or edit_contact.contact_phone
        edit_contact.contact_email = request.form["contact-email"] or edit_contact.contact_email
        edit_contact.contact_address = request.form["contact-address"] or edit_contact.contact_address
        try:
            db.session.commit()
            return redirect("/")
        except Exception as e:
            return f"Operation failed: {e}"
    else:
        return render_template("edit.html", contact=edit_contact)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
