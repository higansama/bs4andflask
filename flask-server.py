from flask import Flask, jsonify
from quotesscraper import ScrapingQuotes
app = Flask(__name__)

@app.route('/')
def hello_world():
    print("helo")
    # listQuote = ScrapingQuotes()
    listQuote = "Helo"
    return jsonify({"quotes": listQuote})

if __name__ == '__main__':
   app.run(debug=True)