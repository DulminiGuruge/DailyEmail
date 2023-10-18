from __future__ import print_function
from urllib import request
import json
import datetime
import datetime
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError




class GetAPIData():
    def __init__(self):

        self.calender_id = ''
        self.open_weather_id = ''
        # If modifying these scopes, delete the file token.json.
        self.SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

  
    

    """
    File read the api key values necessary for security purposes.  
    """
    def read_api_keys(self):
        
        with open("api_keys.txt")as file:
            for line in file:
                data = line.split(',')
                
                if str(data[1]).strip()=="calender_id":
                    self.calender_id= str(data[0])
                if str(data[1]).strip()=="open_weather_api":
                    self.open_weather_id= str(data[0])    
        #get_weather_forecast(coords={'lat': 52.132854, 'lon': -106.631401} )
    """
        Retieve daily weather forecast using the openweather api for the 
        loangitute and latitute of Saskatoon as default.
    """
    def get_weather_forecast(self):
        try: # retrieve forecast for specified coordinates
            coords={'lat': 52.132854, 'lon': -106.631401}
            url = f'https://api.openweathermap.org/data/2.5/forecast?lat={coords["lat"]}&lon={coords["lon"]}&appid={self.open_weather_id}&units=metric'
            data = json.load(request.urlopen(url))
            

            forecast = {'city': data['city']['name'], # city name
                        'country': data['city']['country'], # country name
                        'periods': list()} # list to hold forecast data for future periods

            for period in data['list'][0:9]: # populate list with next 9 forecast periods 
                forecast['periods'].append({'timestamp': datetime.datetime.fromtimestamp(period['dt']),
                                            'temp': round(period['main']['temp']),
                                            'description': period['weather'][0]['description'].title(),
                                            'icon': f'http://openweathermap.org/img/wn/{period["weather"][0]["icon"]}.png'})
            
            print(forecast)

        except Exception as e:
                print(e)   


        """
        Shows basic usage of the Google Calendar API.
        Prints the start and name of the next 10 events on the user's calendar.
        """
    def get_google_calender_api(self):
        
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', self.SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        try:
            service = build('calendar', 'v3', credentials=creds)

            # Call the Calendar API
            today = datetime.date.today()
            timeStart = str(today)+ "T00:00:00Z"
            timeEnd = str(today)+"T23:59:59Z"

            
            print('Getting today\'s events')
            events_result = service.events().list(calendarId=self.calender_id, timeMin=timeStart,timeMax=timeEnd,
                                                singleEvents=True,
                                                orderBy='startTime',timeZone='Canada/Regina').execute()
            events = events_result.get('items', [])

            if not events:
                print('No upcoming events found.')
                return

            # Prints the start and name of the next 10 events
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                print(start, event['summary'])

        except HttpError as error:
            print('An error occurred: %s' % error)

"""
Test the created functions
"""
#get the api keys
data_class=GetAPIData()
data_class.read_api_keys()
data_class.get_weather_forecast()
data_class.get_google_calender_api()


