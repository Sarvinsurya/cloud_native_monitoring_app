import psutil
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/metrics")
def metrics():
    cpu_percent = psutil.cpu_percent()
    mem_percent = psutil.virtual_memory().percent
    return jsonify(cpu_percent=cpu_percent, mem_percent=mem_percent)

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1')
