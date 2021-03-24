from flask import Flask

# create Flask app
app = Flask(__name__)

# default route
@app.route("/")
def hello():
    return "Hello World!"

# run app if this .py is run
if __name__ == "__main__":
    app.run()