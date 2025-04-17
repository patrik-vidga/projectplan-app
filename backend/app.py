from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__, static_folder='../frontend/build', static_url_path='/')
CORS(app)

DATA_PATH = os.path.join(app.root_path, 'data', 'tasks.csv')

@app.route('/api/tasks')
def get_tasks():
    df = pd.read_csv(DATA_PATH)
    df = df.rename(columns={
        'Task Name': 'task',
        'Start': 'start',
        'Finish': 'end'
    })
    return jsonify(df.to_dict(orient='records'))

# Serve React build
@app.route('/')
@app.route('/<path:path>')
def serve(path='index.html'):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)