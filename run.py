from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World! Welcome to my first deployment.'

if __name__ == '__main__':
    app.run(debug=True)