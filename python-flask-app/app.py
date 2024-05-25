from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, world! Now testing'

if __name__ == '__main__':
    app.run()
