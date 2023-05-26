from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/<name>', methods=['GET'])
def hello_name(name):
    return render_template('hello.html', escape(name=name))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)