from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to the Auto-Scaling App!"

@app.route("/load")
def load():
    end = time.time() + 10
    while time.time() < end:
        pass
    return "CPU load generated"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
