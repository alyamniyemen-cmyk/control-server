from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

data_store = {
    "latest_command": "لا يوجد أوامر",
    "device_response": "لا توجد ردود بعد"
}

@app.route('/api/set_command', methods=['POST'])
def set_command():
    req_data = request.json or {}
    data_store["latest_command"] = req_data.get("cmd", "لا يوجد أوامر")
    return jsonify({"status": "success", "command_set": data_store["latest_command"]})

@app.route('/api/get_response', methods=['GET'])
def get_response():
    return jsonify({"response": data_store["device_response"]})

@app.route('/api/get_command', methods=['GET'])
def get_command():
    return jsonify({"command": data_store["latest_command"]})

@app.route('/api/send_response', methods=['POST'])
def send_response():
    req_data = request.json or {}
    data_store["device_response"] = req_data.get("response", "رد فارغ")
    data_store["latest_command"] = "لا يوجد أوامر" 
    return jsonify({"status": "success"})

def handler(request):
    return app(request)
