#! /usr/bin/env python
# encoding: utf-8

"""
Copyright (c) 2014-2015 ourren
author: ourren <i@ourren.com>
"""
import warnings
import requests
import random
from requests.packages.urllib3 import exceptions


def getgeo(ip):
    uas = []
    for line in open("user_agents.txt").readlines():
        if line.strip():
            uas.append(line.strip()[1:-1-1])
    random.shuffle(uas)
    ua = random.choice(uas)  # select a random user agent
    headers = {'User-Agent': ua}
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", exceptions.InsecureRequestWarning)
        r = requests.get("https://db-ip.com/" + str(ip), headers=headers, verify=False)
        if r.status_code == 200 and "Sorry, you have exceeded the daily query limit" not in r.content:
            hostname = ""
            country = ""
            region = ""
            isp = ""
            city = ""
            gps = ""

            f1 = r.content
            if "<th>Hostname</th>" in r.content:
                f1 = r.content.split('<th>Hostname</th>')[1]
                hostname = f1.split('</td>')[0].replace('<td>', '').strip()

            f2 = f1
            if "<th>ISP</th><td>" in f1:
                f2 = f1.split('<th>ISP</th><td>')[1]
                isp = f2.split('</td>')[0].strip()

            f3 = f2
            if "<th>Country</th><td>" in f2:
                f3 = f2.split('<th>Country</th><td>')[1]
                country = f3.split('<img class="flag"')[0].replace("&nbsp;", "").strip()

            f4 = f3
            if "State / Region" in f3:
                f4 = f3.split('<th>State / Region</th><td>')[1]
                region = f4.split('</td>')[0].strip()

            f5 = f4
            if "<th>City</th><td>" in f4:
                f5 = f4.split('<th>City</th><td>')[1]
                city = f5.split('</td>')[0].strip()

            if "<th>Coordinates</th><td>" in f5:
                f6 = f5.split('<th>Coordinates</th><td>')[1]
                gps = f6.split('</td>')[0].strip()

            data = (ip, country, region, city, hostname, isp, gps)
            print data

if __name__ == "__main__":
    for line in open('ip.txt').readlines():
        line = line.strip()
        getgeo(line)