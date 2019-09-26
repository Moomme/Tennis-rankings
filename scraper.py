from selenium import webdriver
import html2text
import json

driver = webdriver.Firefox(executable_path='/home/Alex/Downloads/geckodriver')
driver.get("https://www.atptour.com/en/rankings/singles")

def atp_rankings(): 
    data = driver.find_element_by_class_name('mega-table').get_attribute('innerHTML')

    #print("HELLO OOOO " + str(data))
    h = html2text.HTML2Text()
    h.ignore_links = True

    print(type(data))
    l = h.handle(data).split('|')
    l = [x for x in l if "/" not in x and "\n" not in x]
    print(l)
    print(len(l))
    rankings = [{}]*100
    rank = 0
    lenl = len(l)
    print(lenl)
    for i in range(0, lenl, 5):
        print(i)
        rankings[rank] = {"Name": str(l[i+0]).strip(), "Age": str(l[i+1]).strip(), "Points": str(l[i+2]).strip(), "Tourns": str(l[i+3]).strip(), "Rank": rank+1}
        rank += 1

    #f = open('db.txt.', w)
    fjson = open("db.json", 'w')
    json.dump(rankings, fjson)

def wta_rankings():
    print("WTA Rankings")

def itf_rankings():
    print("ITF Rankings")