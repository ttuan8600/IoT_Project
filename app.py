# app.py

from flask import Flask, request, jsonify, render_template
from database import get_db_connection

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/control', methods=['POST'])
def set_command():
    data = request.get_json()
    command = data.get('command')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE command SET state = ? WHERE id = 1", (command,))
    conn.commit()
    conn.close()

    return jsonify({'status': f'Command set to {command}'})

@app.route('/api/control', methods=['GET'])
def get_command():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT state FROM command WHERE id = 1")
    row = cursor.fetchone()
    conn.close()
    return jsonify({'command': row[0] if row else 'unknown'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
