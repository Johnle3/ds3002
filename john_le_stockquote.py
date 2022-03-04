#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 01:21:08 2022

@author: johnle
"""
#pip install requests
#import requests
#response = requests.get("https://api.open-notify.org/this-api-doesnt-exist")
#print(response.status_code)

#response = requests.get("https://api.open-notify.org/astros.json")
#print(response.status_code)

#print(response.json())

#json.dumps() — Takes in a Python object, and converts (dumps) it to a string.
#json.loads() — Takes a JSON string, and converts (loads) it to a Python object.
#import json
#def jprint(obj):
    # create a formatted string of the Python JSON object
    #text = json.dumps(obj, sort_keys=True, indent=4)
    #print(text)

#jprint(response.json())

#response = requests.get("https://api.open-notify.org/iss-pass.json", params=parameters)

#jprint(response.json())
#%%

import requests
import json 
import pandas as pd 
import sys 
import os 
import getopt

#1. Write a Python Program that accepts user input on a valid Stock Ticker
#2. it can be as many as you like
#3. output is the Long Name of the stock and it's current Price
#4. throw an error code if you can't find that stock
#hint - search/google on accepting inputs from a user ArgV...
#for example this is what it should do

#python3 stockquote.py orcl,tsla,msft
#result would be:
#Oracle Corps: 74.45
#Tesla Motors:  967
#Due Friday at midnight

#print("This is the name of the program:", sys.argv[0])
#print("Number of elements including the name of the program:",
       #len(sys.argv))
#print("Number of elements excluding the name of the program:", len(sys.argv)-1)
#print("Argument List:",str(sys.argv))

url = "https://yfapi.net/v6/finance/quote"
args = sys.argv
stock = sys.argv[1:]
querystring = {"symbols": ','.join(stock)}

headers = {
    'x-api-key': "6GtVhQKubW3oSh3q7cV9q67jDch4P3mM90HaRsP1"
    }
response = requests.request("GET", url, headers=headers, params=querystring)
data = json.loads(response.text)

for i in range(len(stock)):
    print(data['quoteResponse']['result'][i]['longName'] +
          ": " + str(data['quoteResponse']['result'][i]['regularMarketPrice']))
    #print('error cannot find stock')
# $ python API_Intro.py


#python API_Intro.py argument1 argument2 "hello world"


# load to dictionary json.loads(response.text) 
#def get_stockquote(x):
    #response = requests.request("GET", url, headers=headers, params=querystring)
    #for x in data:
        #if x['symbol'] == stock:
            #return x['longName','ask']


#company = get_stockquote(stock)

#print(company)    