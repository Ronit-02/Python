from flask import Flask
app = Flask(__name__)    # flask constructor (takes curr module as input)


@app.route('/')   #  which url should call the associated function, route(rule, options)
def f1():
    return 'Welcome!'

@app.route('/hello/<name>')  # dynamic routing
def f2(name):
    return 'Hello %s' % name


if __name__ == '__main__':
    app.run(debug=True)  # app.run(host, port, debug, options)