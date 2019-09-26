from flask import Flask, escape, request, render_template
from apscheduler.schedulers.background import BackgroundScheduler
from scraper import atp_rankings, wta_rankings, itf_rankings
import json

app = Flask(__name__)

# This should be weekly in prod as rankings change weekly 
SCRAPER_INTERVAL = 10

@app.route('/')
def first():
    return render_template('firstpage.html')


@app.route('/atp')
def tennis():
    rankings = json.load(open('db.json'))
    return  render_template('rankings.html', rankings=rankings, system='ATP')

if __name__ == '__main__':
    # In debug mode flask initilizes the app twice and therefore each job will be registered twice. 
    # This will not be a problem in prod
    scheduler = BackgroundScheduler()
    scheduler.add_job(atp_rankings, 'interval', seconds=SCRAPER_INTERVAL)
    scheduler.add_job(wta_rankings, 'interval', seconds=SCRAPER_INTERVAL)
    scheduler.add_job(itf_rankings, 'interval', seconds=SCRAPER_INTERVAL)
    scheduler.start()

    app.run(debug=True)