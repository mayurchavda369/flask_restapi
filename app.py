from flask import Flask
app = Flask(__name__)
app.debug=True

@app.route("/")
def welcome():
    return "hello its working fine"
@app.route("/home")
def home():
    return "hello its working good"

from controller import *

# if __name__ == "__main__":
#     app.run(debug=True)