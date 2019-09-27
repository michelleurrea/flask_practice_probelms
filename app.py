from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

@app.route('/greeting')
def greeting():
    return render_template('index.html', name='Akilah')

@app.route('/pie')
def pie():
    return jsonify({'pie ingredient': 'ingredients[0]'})

if __name__ == '__main__':
    app.run()