from flask import Flask 
import os
app = Flask(__name__)

@app.route("/")
def home():
    return("<h1><center>Customer Care Registry</center></h1>")

if __name__ == "__main__":
    port = os.environ.get("PORT",5000)
    app.run(debug = True, port=port,host="0.0.0.0")