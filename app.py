from flask import Flask
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def hello():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
    return f"""
    <html>
        <head><title>Dr. ViKi DevOps Pipeline</title></head>
        <body style="font-family: Arial; text-align: center; margin-top: 100px;">
            <h1>Hello from Dr. ViKi DevOps Pipeline!</h1>
            <p>Current timestamp: {timestamp}</p>
            <p>Version: 1.0</p>
        </body>
    </html>
    """

@app.route('/health')
def health():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)