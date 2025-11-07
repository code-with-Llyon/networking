from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello everyone — this is my containerized networking app! (Built with Flask)"

@app.route("/health")
def health():
    return {"status": "ok"}, 200

@app.route("/favicon.ico")
def favicon():
    return "", 204

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
