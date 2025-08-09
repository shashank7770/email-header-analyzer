from flask import Flask, render_template, request
from utils import parse_email_header

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    raw_header = request.form.get('email_header')
    parsed_data = parse_email_header(raw_header)
    return render_template('result.html', data=parsed_data)

if __name__ == '__main__':
    app.run(debug=True)
