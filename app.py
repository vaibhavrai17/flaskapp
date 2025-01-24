from flask import Flask ,jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, Azure Flask App!'

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200



@app.route('/message')
def message():
    return 'this is a message'


if __name__ == '__main__':
    app.run(debug=True)
