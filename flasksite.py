from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def first():
    return "<h1>First page<h1>"

@app.route('/second')
def second():
    return '<h1>First page<h1>'

@app.route('/tennis')
def tennis():
    # name = request.args.get("name", "Mohammad 2")
    rankings = eval(open("db.txt", 'r').read())
    retStr = ""
    lenR = len(rankings)
    for i in range(lenR):
        player_dict = rankings[i]
        retStr += "<p>" + str(i+1) + ". Name: " + player_dict["Name"] + ", Age: " + player_dict["Age"] + ", Points: " + player_dict["Points"] + ", Tournaments Played: " + player_dict["Tourns Played"] + " </p>"
    return  retStr + str(rankings)

if __name__ == '__main__':
    app.run(debug=True)