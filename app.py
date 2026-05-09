from flask import Flask, jsonify
import psutil

app = Flask(__name__)

@app.route('/system')
def system_info():
    data = {
        "cpu_percent": psutil.cpu_percent(),
        "memory_percent": psutil.virtual_memory().percent
    }
    return jsonify(data)

@app.route('/health')
def health():
    return jsonify({
        "status": "running"
    })

if __name__ == '__main__':
    app.run(debug=True)
