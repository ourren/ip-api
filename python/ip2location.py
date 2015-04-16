#! /usr/bin/env python
# encoding: utf-8

"""
Copyright (c) 2014-2015 ourren
author: ourren <i@ourren.com>
"""
import requests
import random

def getgeo(ip):
    uas = []
    for line in open("user_agents.txt").readlines():
        if line.strip():
            uas.append(line.strip()[1:-1-1])
    random.shuffle(uas)
    ua = random.choice(uas)  # select a random user agent
    headers = {'User-Agent': ua}
    r = requests.get("http://www.ip2location.com/demo/" + str(ip), headers=headers, verify=False)
    if r.status_code == 200:
        hostname = ""
        country = ""
        region = ""
        isp = ""
        city = ""
        gps = ""

        f1 = r.content
        if "<td><b>Location</b></td>" in f1:
            f2 = f1.split('<td><b>Location</b></td>')[1]
            location = f2.split('align="absMiddle" />')[1].split('</td>')[0].strip()
            location = location.split(',')
            if len(location) == 3:
                country = location[0]
                region = location[1]
                city = location[2]
            elif len(location) == 2:
                country = location[0]
                city = location[1]
            elif len(location) == 1:
                country = location[0]

        f2 = f1
        if "<td><b>Latitude & Longitude</b></td>" in f2:
            f2 = f2.split('<td><b>Latitude & Longitude</b></td>')[1]
            gps = f2.split('</td>')[0].replace('<td style="vertical-align:middle;">', '').replace("&nbsp;", " ").strip()

        f3 = f2
        if "<td><b>ISP</b></td>" in f3:
            f3 = f3.split('<td><b>ISP</b></td>')[1]
            hostname = f3.split('</td>')[0].replace('<td style="vertical-align:middle;">', '').strip()

        f4 = f3
        if "<td><b>Domain</b></td>" in f4:
            f4 = f4.split('<td><b>Domain</b></td>')[1]
            hostname = f4.split('</td>')[0].replace('<td style="vertical-align:middle;">', '').strip()

        data = (ip, country, region, city, hostname, isp, gps)
        print data

if __name__ == "__main__":
    for line in open('ip.txt').readlines():
        line = line.strip()
        getgeo(line)