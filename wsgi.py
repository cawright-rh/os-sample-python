from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World! This is a test of a change"

if __name__ == "__main__":
    application.run()
