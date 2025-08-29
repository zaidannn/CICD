from flask import Flask, jsonify, request

app = Flask(__name__)

# fungsi helper untuk dites langsung
def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

@app.route("/")
def home():
    return jsonify({"message": "Hello, DevOps!"})

@app.route("/add", methods=["GET"])
def add_numbers():
    try:
        a = int(request.args.get("a", 0))
        b = int(request.args.get("b", 0))
        return jsonify({"result": add(a, b)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400
