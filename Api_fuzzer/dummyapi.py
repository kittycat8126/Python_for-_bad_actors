from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# ---------- UTILITY ---------
SQLI_PATTERN = r"('|--|;| OR | AND )"

def looks_like_sqli(val):
    return re.search(SQLI_PATTERN, val, re.IGNORECASE) is not None

# ---------- ROUTES ---------

@app.route("/")
def index():
    return jsonify({"message": "Dummy API root"}), 200


# ---------------- USERS ENDPOINT -----------------
@app.route("/users", methods=["GET"])
def users():

    # Required parameter: id
    user_id = request.args.get("id")

    if user_id is None:
        return jsonify({"error": "Missing required parameter: id"}), 422

    # Check for SQL injection patterns
    if looks_like_sqli(user_id):
        return jsonify({"error": "Database error detected"}), 500

    # Validate type
    if not user_id.isdigit():
        return jsonify({"error": "ID must be numeric"}), 400

    # Valid ID?
    if int(user_id) > 1000:
        return jsonify({"error": "User not found"}), 404

    return jsonify({
        "status": "OK",
        "user": {"id": user_id, "name": "test-user"}
    }), 200


# ---------------- LOGIN ENDPOINT -----------------
@app.route("/auth/login", methods=["POST"])
def login():
    data = request.json if request.is_json else {}

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 422

    if looks_like_sqli(username) or looks_like_sqli(password):
        return jsonify({"error": "Authentication backend crashed"}), 500

    if username == "admin" and password == "admin123":
        return jsonify({"token": "fake-jwt-token"}), 200

    return jsonify({"error": "Invalid credentials"}), 401


# ---------------- SEARCH ENDPOINT -----------------
@app.route("/search")
def search():
    q = request.args.get("q", "")

    if looks_like_sqli(q):
        return jsonify({"error": "Search backend failure"}), 500

    if len(q) < 2:
        return jsonify({"error": "Query too short"}), 400

    return jsonify({"results": [f"Result for {q}"]}), 200


# ------------- 404 Handler ---------------
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not Found"}), 404


if __name__ == "__main__":
    app.run(port=3000, debug=True)
