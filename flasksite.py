from flask import Flask, escape, request, render_template
import json

app = Flask(__name__)

@app.route('/')
def first():
    return render_template('firstpage.html')


@app.route('/atp')
def tennis():
    rankings = json.load(open('db.json'))
    return  render_template('rankings.html', rankings=rankings, system='ATP')

if __name__ == '__main__':
    app.run(debug=True)