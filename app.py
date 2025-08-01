from flask import Flask, request, jsonify
from rule_engine import classify

app = Flask(__name__)

@app.route("/status", methods=["POST"])
def get_status():
    data = request.get_json()
    sensor_type = data.get("sensor_type")
    value = data.get("value")

    if sensor_type is None or value is None:
        return jsonify({"error": "Missing sensor_type or value"}), 400

    status, message = classify(sensor_type, value)

    return jsonify({
        "sensor_type": sensor_type,
        "value": value,
        "status": status,
        "message": message
    })

if __name__ == "__main__":
    app.run(debug=True)
