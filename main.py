from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/content')
def content():
    # Your code to render content.html goes here
    return render_template('content.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0")
