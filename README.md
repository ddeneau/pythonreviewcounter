# Python Review Counter (Smiirl JSON URL Flask application)

This is a simple Flask Python web-application that makes API calls, and provides a JSON response for the counting device: https://www.smiirl.com
Usually, this is just any number, with the response being, literally { "number": 21 }. Of course, you should use an API to get a useful number. 
In this case, the project is configured to use the Google Maps API, and get the number of reviews for a business.

# How to Use

You'll need the following:

A Google Developer Account. Follow the steps here (https://developers.google.com/maps?authuser=2#:~:text=Contact%20Sales-,Get%20Started,-Build%20awesome%20apps) 
to register, and obtain an API Key.
In App.Py, enter your API Key as a string. (replace MYAPIKEY)

The PlaceID of a business. Enter the PlaceID as a string in the app.py. (replace MYPLACEID)

A Heroku account (or another hosting solution). Deploy this project to Heroku so that you can provide the Smiirl device with a working, URL.
