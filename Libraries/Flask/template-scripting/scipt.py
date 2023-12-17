from flask import Flask, render_template
app = Flask(__name__)


@app.route('/user/<uname>/<int:num>')
def hello(uname, num):
    return render_template('index.html', name = uname, n = num)


if __name__ == '__main__':
    app.run(debug=True)