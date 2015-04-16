#! /usr/bin/env python
# encoding: utf-8

"""
Copyright (c) 2014-2015 ourren
author: ourren <i@ourren.com>
"""
import requests
import json
import random
import time

def getgeo(ip):
    uas = []
    for line in open("user_agents.txt").readlines():
        if line.strip():
            uas.append(line.strip()[1:-1-1])
    random.shuffle(uas)
    ua = random.choice(uas)  # select a random user agent
    headers = {'User-Agent': ua}
    r = requests.get("http://ip-api.com/json/" + str(ip), headers=headers, verify=False)
    if r.status_code == 200 and "Sorry, you have exceeded the daily query limit" not in r.content:
        hostname = ""
        country = ""
        region = ""
        isp = ""
        city = ""
        gps = ""
        organization = ""
        asname = ""

        ret = json.loads(r.content)
        if ret["status"] == "success":
            country = ret["country"]
            region = ret["region"]
            city = ret["city"]
            isp = ret["isp"]
            gps = str(ret["lat"]) + " " + str(ret["lon"])
            organization = ret["org"]
            asname = ret["as"]

        data = (ip, country, region, city, hostname, isp, gps, organization, asname)
        print data

if __name__ == "__main__":
    for line in open('ip.txt').readlines():
        line = line.strip()
        getgeo(line)
        time.sleep(1)