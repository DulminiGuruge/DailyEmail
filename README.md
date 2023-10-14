## Send Daily Emails using API's calls

#### Create the virtual environment for PyQt5

First create a virtual environment using the below command in the terminal.

>python3 -m venv venv

Then you will see a folder named 'venv'. Then we need to activate the virtaul environment by runningthe activate file inside venv/bin path. We can use the below command to activate the virtual environment in mac.

> source venv/bin/activate

Then install PyQt5 library using pip command.

>pip install PyQt5


#### Get details from the weather api

1. Go to https://openweathermap.org/api and create an account to get the weather api. 
2. I choose **5 Day / 3 Hour Forecast** option and subscribed for free get api key.  


#### Accessing google calender api key

1. First go to the this link. https://developers.google.com/calendar/api/quickstart/python
2. Then create a google cloud project - https://developers.google.com/workspace/guides/create-project
3. Add a project name and then choose create button. Then go to Api & Services, then Enable 'Api's & services'
4. Then click on the Enable Api & services which is the top tab on the screen and search for google api. Then search for calender in the search bar.
5. Choose Google Calender Api and click on the enable button.
6. Then select the OAuth consent screen. Choose External and select Create.
7. Then fill app name, user support email and add an email for developer contact information. Then save and go to add or remove scopes. Then select all the Google Calender Api related fields and update.
8. Then save and go to credentials in the left side panel and choose 'create credential' button at the top of the tab. Choose OAuth client ID and select Desktop app as the application type and Create a name, I used Desktop client 1.Then click on create.
9. Now download the json file and save in the same folder where the code exists and rename it to credentials.json.
10. Go to the OAuth consent screen and add your email as the test user in using the add users button.
11. Install the google client library for python. pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
12. Now use the code in python quick start for Calender Api.
