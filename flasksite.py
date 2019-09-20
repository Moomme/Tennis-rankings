from flask import Flask, escape, request

app = Flask(__name__)
@app.route('/')
def hello():
    name = request.args.get("name", "Mohammad")
    return f'<h1>Hello, {escape(name)}!<h1>'

@app.route('/second')
def second():
    name = request.args.get("name", "Mohammad 2")
    return f'<h1>Hello, {escape(name)}!<h1>'

@app.route('/tennis')
def tennis():
    # name = request.args.get("name", "Mohammad 2")
    dict = eval(open("db.txt", 'r').read())
    return str(dict)
if __name__ == '__main__':
    app.run(debug=True)