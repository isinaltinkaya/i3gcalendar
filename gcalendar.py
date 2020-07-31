#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Google Calendar notifier for i3blocks
# by Isin Altinkaya
#
# Usage at i3blocks.config:
#
# [gcalendar]
# command=/PATH_TO_SCRIPT/gcalendar.py token.json
# label=
# interval=1
#
#
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'

# Change following path with your /PATH_TO_FILE/token.json
store = file.Storage('/PATH_TO_FILE/token.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('calendar', 'v3', http=creds.authorize(Http()))

# Call the Calendar API
now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
# Get the closest event
events_result = service.events().list(calendarId='primary', timeMin=now,maxResults=1, singleEvents=True, orderBy='startTime').execute()
events = events_result.get('items', [])

if not events:
    print('No upcoming events')
    print('No upcoming events')

for event in events:
    start = event['start'].get('dateTime', event['start'].get('date'))

if int(start[8:10]) == int(datetime.datetime.now().strftime('%d')) and int(start[5:7]) == int(datetime.datetime.now().strftime('%m')):
    date_info = "Today"
elif int(start[8:10]) == int(datetime.datetime.now().strftime('%d'))+1 and int(start[5:7]) == int(datetime.datetime.now().strftime('%m')):
    date_info = "Tomorrow"
else:
    date_info = "on " + start[8:10] + "." + start[5:7]

print(date_info, "at",  start[11:16], event['summary'])
print(date_info, "at",  start[11:16], event['summary'])
print(" ")
