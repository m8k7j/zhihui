from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Patsnap'

if __name__ == '__main__':
    app.run(host='192.168.35.217')
