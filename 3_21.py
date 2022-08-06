from flask import Flask, request, jsonify

app = Flask("answer")

@app.route("/ab/search")
def search():
    search_query = request.args.to_dict()
    response_name = request.args["Name"]
    response_rate = request.args["Rate"]
    response = "{'Name':'"+response_name+",'Rate':'"+ response_rate+"'}"
    return jsonify(response)