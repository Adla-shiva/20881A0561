import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/numbers', methods=['GET'])
def get_numbers():
    urls = request.args.getlist('url')
    results = []

    for url in urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                if 'numbers' in data:
                    numbers = data['numbers']
                    results.extend(numbers)
            else:
                app.logger.warning(f"Error retrieving data from URL: {url}. Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            app.logger.warning(f"Request error for URL: {url}. Error: {str(e)}")

    return jsonify({'numbers': results})

if __name__ == '__main__':
    app.run(port=8008, debug=True)
