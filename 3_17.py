from flask import Flask, jsonify

FIELDS = ["Name", "City", "Skill", "Rate", "Phone"]

app = Flask("answer")

@app.route("/fields")
def fields():
    response = jsonify(FIELDS)
    return response