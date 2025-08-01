import json
import logging

logging.basicConfig(filename="rule_engine.log", level=logging.DEBUG)

try:
    with open("config.json", "r") as f:
        RULES = json.load(f)
except Exception as e:
    logging.error("Could not load config: " + str(e))
    RULES = {}

def classify(sensor_type, value):
    if sensor_type not in RULES:
        logging.warning(f"Missing rule for sensor type: {sensor_type}")
        return "OK", "No rule defined"

    try:
        min_val = RULES[sensor_type]["min"]
        max_val = RULES[sensor_type]["max"]

        if value < min_val or value > max_val:
            return "Critical", ""
        elif value < min_val + 5 or value > max_val - 5:
            return "Warning", ""
        else:
            return "OK", ""
    except Exception as e:
        logging.error(f"Error in classifying {sensor_type}: {e}")
        return "OK", "Error in rule logic"
