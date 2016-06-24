#Parser for html
from lxml import html
#For Notifications on your desktop
from gi.repository import Notify
import requests
import time
#download the cricbuzz library and do pip install cricbuzz
from cricbuzz import *
#The Twilio API
from twilio.rest import TwilioRestClient

def func():
 #Enter your Twilio accountSid and authToken
 accountSid = ""
 authToken = ""
 #Parser for the Cricbuzz XML Page in cricbuzz library
 cric = CricbuzzParser()
 #Connecting to the Twilio API
 twilioClient = TwilioRestClient(accountSid, authToken)
 myTwilioNumber = ""
 destCellPhone = ""
 #Getting the XML File and extracting the matches from it
 match = cric.getXml()
 details = cric.handleMatches(match)
 #Filtering out the NoneType Objects in 'details'
 details = filter(None,details)
 message = 'No Match Available'
 for i in details:
 #Traversing the list
      if 'Match State' in i:
      #If the match state key is present in the dict
         if i['Match State'] == 'inprogress':
          #If the match is in progress
             message =  i['Team']+ "      "+ i['Match Format'] + ' Match at ' + i['Venue']+  "\n" +i['Batting team'] + ' ' + i['Batting Team Runs'] + '/'+i['Batting Team Wickets'] + '  Overs: ' + i['Batting Team Overs']
 #Generates the message 
 Notify.init("Live Scores")
 #Shows Notification on the desktop
 Notify.Notification.new("Match currently in progress:",message).show()
 #Sends message to the phone number
 myMessage = twilioClient.messages.create(body = "Match Currently in progress: " + message, from_=myTwilioNumber, to=destCellPhone)
 #Defines an interval of 60 seconds
 time.sleep(60)
while True:
 func()
