from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/what')
def what():
    return "What are we doing for the hackathon?"

if __name__ == '__main__':
    app.run()
