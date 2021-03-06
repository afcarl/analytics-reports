from app import app
from flask import render_template,request
import json

def load_dump(filename):
    return json.dumps(json.load(open("reports/"+filename,"r")))

@app.route("/all-domains-30-days.json",methods=["GET","POST"])
def all_domains_30_days():
    return load_dump("all-domains-30-days.json")

@app.route("/device_model.json",methods=["GET","POST"])
def device_model():
    return load_dump("device_model.json")

@app.route("/language.json",methods=["GET","POST"])
def language():
    return load_dump("language.json")

@app.route("/os.json",methods=["GET","POST"])
def os():
    return load_dump("os.json")

@app.route("/screen-size.json",methods=["GET","POST"])
def screen_size():
    return load_dump("screen-size.json")

@app.route("/today.json",methods=["GET","POST"])
def today():
    return load_dump("today.json")

@app.route("/top-domains-30-days.json",methods=["GET","POST"])
def top_domains_30_days():
    return load_dump("top-domains-30-days.json")

@app.route("/top-downloads-yesterday.json",methods=["GET","POST"])
def top_downloads_yesterday():
    return load_dump("top-downloads-yesterday.json")

@app.route("/top-pages-30-days.json",methods=["GET","POST"])
def top_pages_30_days():
    return load_dump("top-pages-30-days.json")

@app.route("/top-traffic-sources-30-days.json",methods=["GET","POST"])
def top_traffic_sources_30_days():
    return load_dump("top-traffic-sources-30-days.json")

@app.route("/windows-browsers.json",methods=["GET","POST"])
def windows_browsers():
    return load_dump("windows-browsers.json")

@app.route("/all-pages-realtime.json",methods=["GET","POST"])
def all_pages_realtime():
    return load_dump("all-pages-realtime.json")

@app.route("/devices.json",methods=["GET","POST"])
def devices():
    return load_dump("devices.json")

@app.route("/last-48-hours.json",methods=["GET","POST"])
def last_48_hours():
    return load_dump("last-48-hours.json")

@app.route("/realtime.json",methods=["GET","POST"])
def realtime():
    return load_dump("realtime.json")

@app.route("/second-level-domains.json",methods=["GET","POST"])
def second_level_domains():
    return load_dump("second-level-domains.json")

@app.route("/top-cities-realtime.json",methods=["GET","POST"])
def top_cities_realtime():
    return load_dump("top-cities-realtime.json")

@app.route("/top-domains-7-days.json",methods=["GET","POST"])
def top_domains_7_days():
    return load_dump("top-domains-7-days.json")

@app.route("/top-exit-pages-30-days.json",methods=["GET","POST"])
def top_exit_pages_30_days():
    return load_dump("top-exit-pages-30-days.json")

@app.route("/top-pages-7-days.json",methods=["GET","POST"])
def top_pages_7_days():
    return load_dump("top-pages-7-days.json")

@app.route("/usa.json",methods=["GET","POST"])
def usa():
    return load_dump("usa.json")

@app.route("/windows-ie.json",methods=["GET","POST"])
def windows_ie():
    return load_dump("windows-ie.json")

@app.route("/browsers.json",methods=["GET","POST"])
def browsers():
    return load_dump("browsers.json")

@app.route("/ie.json",methods=["GET","POST"])
def ie():
    return load_dump("ie.json")

@app.route("/os-browsers.json",methods=["GET","POST"])
def os_browsers():
    return load_dump("os-browsers.json")

@app.route("/reports.json",methods=["GET","POST"])
def reports():
    return load_dump("reports.json")

@app.route("/sites.json",methods=["GET","POST"])
def sites():
    return load_dump("sites.json")

@app.route("/top-countries-realtime.json",methods=["GET","POST"])
def top_countries_realtime():
    return load_dump("top-countries-realtime.json")

@app.route("/top-downloads-7-days.json",methods=["GET","POST"])
def top_downloads_7_days():
    return load_dump("top-downloads-7-days.json")

@app.route("/top-landing-pages-30-days.json",methods=["GET","POST"])
def top_landing_pages_30_days():
    return load_dump("top-landing-pages-30-days.json")

@app.route("/top-pages-realtime.json",methods=["GET","POST"])
def top_pages_realtime():
    return load_dump("top-pages-realtime.json")

@app.route("/users.json",methods=["GET","POST"])
def users():
    return load_dump("users.json")

@app.route("/windows.json",methods=["GET","POST"])
def windows():
    return load_dump("windows.json")
