from flask import Flask, request

app = Flask("answer")

@app.route("/ab/developer/<developer_id>/field", methods=["POST"])
def new_field(developer_id):
    field_name = request.json["name"]
    return f"Name {field_name}, developer: {developer_id}"