from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return 'hello {}'.format(name)


@app.route('/f')
@app.route('/f/<celsius>')
def c_to_f(celsius=""):
    result = float(celsius) * 9.0 / 5 + 32
    return "{} celsius is equal to {} fahrenheit ".format(str(celsius), str(result))
if __name__ == '__main__':
    app.run()
