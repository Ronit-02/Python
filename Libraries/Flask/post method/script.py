from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/')
def customer(): 
    return render_template('customer.html')


@app.route('/success', methods=['POST'])  # POST does not send data to 'url'
def login():
    uname = request.form['uname']    # only for name
    result = request.form           # for all details
    return render_template('result.html', result = result, name = uname)


if __name__ == '__main__':
    app.run(debug=True)