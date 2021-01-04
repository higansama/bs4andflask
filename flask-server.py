from flask import Flask, jsonify
from quotesscraper import ScrapingQuotes
app = Flask(__name__)

@app.route('/index')
def hello_world():
    listQuote = ScrapingQuotes()
    return jsonify({"quotes": listQuote})


@app.route('/boo/')
def boo():
    print("helo")
    return jsonify({"quotes": "boo"})

if __name__ == '__main__':
   app.run(debug=True, port=3000)