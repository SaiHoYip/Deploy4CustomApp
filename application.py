from flask import Flask, request, Response
from flask import render_template
import json
import help
import sqlite3

application = app = Flask(__name__)

@app.route("/", methods=["POST", "Get"])
def sub_budget():
    Spent = ""
    Budget = ""
    if request.method == "POST" and "Spent" in request.form and "Budget" in request.form:
    # Get item from the POST body
        Spent = str(request.form.get("Spent"))
        Budget = str(request.form.get("Budget"))
        slot_id = str(request.form.get("slot_id"))
        req_data = request.get_json()
        help.Subtraction(Budget, Spent, slot_id)

    cat = sqlite3.connect('Budget.db')
    db = cat.cursor()
    rows = db.execute('SELECT * FROM Budgee')
    ro = rows.fetchall()

    # Return response
    return render_template("home.html", Spent = "Spent", Budget= "Budget", slot_id="slot_id", ro=ro)

@app.route("/delete", methods=["POST", "GET"])
def delete_item():
    slot_id = 0
    if request.method == "POST" and "slot_id" in request.form:
        slot_id = str(request.form.get("slot_id"))
        req_data = request.get_json()
        help.Delete(slot_id)

    cat = sqlite3.connect('Budget.db')
    db = cat.cursor()
    rows = db.execute('SELECT * FROM Budgee')
    ro = rows.fetchall()
    return render_template("home.html", ro=ro)

app.run(debug=1)