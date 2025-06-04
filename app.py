from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    current_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')
    user_ip = request.remote_addr
    return jsonify({
        "message": "Hello from Flask!",
        "current_time": current_time,
        "your_ip": user_ip
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
