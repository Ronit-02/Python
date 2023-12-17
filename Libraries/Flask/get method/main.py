from flask import Flask, request
app = Flask(__name__)


@app.route('/login', methods=['GET'])
def login():
    uname = request.args.get('uname')
    passwd = request.args.get('pass')
    if uname == 'ronit' and passwd == 'admin':
        return 'Welcome %s ' % uname
    else:
        return 'Try again!' 


if __name__ == '__main__':
    app.run(debug=True)