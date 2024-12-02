import json
import random
from flask import Flask, request, jsonify

# find the path of the data.json file
# with open('data.json') as f:
#     data = json.load(f)
#     print(data)

data = [
     {
         "name": "apple"
    },
     {
         "name": "banana"
     },
     {
         "name": "orange"
     },
     {
         "name": "grapes"
     }
 ]

# read data.json from the auto_suggest folder




with open('/data.json') as f:
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