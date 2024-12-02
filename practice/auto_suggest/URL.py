import json
import random
from flask import Flask, request, jsonify







with open(r'C:\Users\Public\Documents\VS CODE Workspace\skill-copilot-codespaces-vscode\practice\auto_suggest\data.json') as f:
    data = json.load(f)

app = Flask(__name__)

@app.route('/auto_suggest', methods=['GET'])
def auto_suggest():
    query = request.args.get('query')
    results = []
    for item in data:
        if query in item['name']:
            results.append(item['name'])
    return jsonify(random.sample(results, 5))

if __name__ == '__main__':
    app.run(debug=True)