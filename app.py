#!/bin/python

from flask import Flask, render_template
import requests
import key

app = Flask(__name__)

@app.route("/")
def weather():
    
    password = key.keycode
       
    city = "Tokyo"
    url = ("http://api.openweathermap.org/data/2.5/forecast?q={}&units=imperial&appid=" + password )

    r = requests.get(url.format(city)).json()
    
    weather = {
        
        'city' : city,
        'temperature' : round(r['list'][0]['main']['temp']),
        'description' : r['list'][0]['weather'][0]['description'],
        'icon' : r['list'][0]['weather'][0]['icon'],
        
    }
    
    print (weather)
    
    return render_template('index.html', weather=weather)
    
app.run()


"""
    if response.json()['cod'] == "404":
        
        print ("Was there a typo? Try again!")
        weather()
        
    else: 
    
        temp = round(response.json()['list'][0]['main']['temp'])
        feelslike = round(response.json()['list'][0]['main']['feels_like'])
        humidity = response.json()['list'][0]['main']['humidity']
        weather = response.json()['list'][0]['weather'][0]['main']
        info = response.json()['list'][0]['weather'][0]['description']
        degree_sign = u"\N{DEGREE SIGN}"

        print (f"\nIt is currently {temp}{degree_sign}F in {city} with {info}. It feels like {feelslike}{degree_sign}F, with a humidity of {humidity}%. \n")
"""

