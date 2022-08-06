from flask import Flask, request

app = Flask("search")

@app.route("/search")
def search():
    try:
        developer_name = request.args["name"]
        return f"Search for {developer_name}"
    except KeyError:
        return "Nothing given"