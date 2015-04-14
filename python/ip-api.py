#! /usr/bin/env python
# encoding: utf-8

"""
Copyright (c) 2014-2015 ourren
author: ourren <i@ourren.com>
"""
import requests
import json
import time

def getgeo(ip):
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1;'}
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