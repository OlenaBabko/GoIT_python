from flask import Flask, jsonify

developer = {"Name": "Peter", "Rate": "1800"}

app = Flask("developer")


@app.route("/developer")
def developer_out():
    response = jsonify(developer)  
    return response