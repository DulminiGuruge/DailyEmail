## Automate Daily Emails in Python

This PyQt5-based desktop application allows users to automate the sending of daily emails to a pre-selected list at a scheduled time. The application sends daily weather reports and the user's daily events extracted using API calls, providing a comprehensive and convenient method for staying up-to-date.

### Technologies used
1. PyQt5 to create the GUI
2. Python for calling APIs


### Create the virtual environment for PyQt5

First, create a virtual environment using the below command in the terminal.

>python3 -m venv venv

Then, you will see a folder named 'venv'. Then, we must activate the virtual environment by running the activate file inside the venv/bin path. We can use the below command to activate the virtual environment in Mac.

> source venv/bin/activate

Then, install the PyQt5 library using the pip command.

>pip install PyQt5


### Get details from the weather API

1. Go to https://openweathermap.org/api and create an account to get the weather API. 
2. I chose **5 Day / 3 Hour Forecast** option and subscribed for free to get the API key.  


### Accessing Google calender API key

1. First, go to this link. https://developers.google.com/calendar/api/quickstart/python
2. Then create a Google Cloud project - https://developers.google.com/workspace/guides/create-project
3. Add a project name and then choose the Create button. Then go to Api & Services, then Enable 'APIs & services.'
4. Then click Enable API & services, the top tab on the screen and search for Google API. Then, search for the calendar in the search bar.
5. Choose Google Calender API and click on the enable button.
6. Then select the OAuth consent screen. Choose External and select Create.
7. Then fill in the app name and user support email and add an email for developer contact information. Then save and go to add or remove scopes. Then select all the Google Calender Api-related fields and update.
8. Then save and go to credentials in the left side panel and choose the 'create credential' button at the top of the tab. Choose OAuth client ID, select Desktop app as the application type and Create a name; I used Desktop client 1. Then click on Create.
9. Now download the JSON file, save it in the same folder where the code exists and rename it to credentials.json.
10. Go to the OAuth consent screen and add your email as the test user using the add users button.
11. Install the Google client library for Python. pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
12. Now use the code in Python quick start for Calender API.

Sending emails with HTML

I refered https://realpython.com/python-send-email/ to learn about this.
