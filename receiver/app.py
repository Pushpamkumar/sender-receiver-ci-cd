from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "✅ Receiver is running"

@app.route("/message", methods=["POST"])
def receive():
    data = request.get_json()
    print(f"📨 Message received: {data}")
    return {"status": "received", "message": data}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
