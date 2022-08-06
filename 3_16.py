from flask import Flask

app = Flask("start")


@app.route("/hello")
def fields():
    response = "Hello, World! I have startup!"
    return response


if __name__ == '__main__':
    app.run()