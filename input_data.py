# Code used to parse and clean crime incident data (csv format), 
# and use Geocoding API to generate latitude and longitude from street addesses

import glob
import argparse
import os, sys
import re
WORD = re.compile(r"[^(|,|'|\s|)]+")
#WORD = re.compile(r"[\w+-/]+")
import subprocess
import csv
import requests

key = "AIzaSyCUV9mE32gI0uU2CpKcYjPXJbXliyTWrKo"

if __name__ == '__main__':

    # Get input/output files from user
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='File to load Amazon review data from')
    parser.add_argument('output_file', help='File to load Amazon review data from')


    args = parser.parse_args()

    fw = open(args.output_file, 'w')

    fr = open(args.input_file, 'r', )
    for line in fr:
        if (line != "\n"):
            row = line.split(",")
            row[2] = re.sub("BLOCK ", "", row[2]) + " Champaign IL"
            add_arr = row[2].split(' ')

            url_add = ""
            i = 1
            url_add += add_arr[0]
            while i < len(add_arr):
                url_add += "+" + add_arr[i]
                i += 1

            url = "https://maps.googleapis.com/maps/api/geocode/json?key="+key+"&address="+url_add
            req_json = requests.get(url).json()


            date_time = row[3].split(' ')
            date = date_time[0]
            date_s = date.split("/")
            date_string = date_s[2]+"-"+date_s[1]+"-"+date_s[0]
            # date_t = date(int(date_s[0]), int(date_s[1]), int(date_s[2])).isoformat()

            time = str(date_time[1])+ ":00"

            lat = req_json["results"][0]["geometry"]["location"]["lat"]
            lng = req_json["results"][0]["geometry"]["location"]["lng"]
            fw.write(""+row[4] +","+ row[1]+ ","+ row[2] +","+str(lat)+","+str(lng)+ ","+ str(date_string) +","+time+"\n")

    fw.close()

    fr.close()
