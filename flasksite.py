from flask import Flask, escape, request
from selenium import webdriver
import html2text

h = html2text.HTML2Text()
h.ignore_links = True

app = Flask(__name__)

driver = webdriver.Firefox()
driver.get("https://www.atptour.com/en/rankings/singles")
data = driver.find_element_by_class_name('mega-table').get_attribute('innerHTML')

#print("HELLO OOOO " + str(data))

print(type(data))
l = h.handle(data).split('|')
l = [x for x in l if "/" not in x and "\n" not in x]
print(l)
print(len(l))
retStr = ""
i = 1
while len(l) > 0:
    retStr += "<p>" + str(i) + ". Name: " + l[0] + ", Age: " + l[1] + ", Points: " + l[2] + ", Tourns Played: " + l[3] + "</p>"
    i += 1
    l = l[5:]

print(retStr)
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
    return retStr
if __name__ == '__main__':
    app.run(debug=True)