# i3gcalendar

A script to see the closest event in your Google Calendar on your i3blocks bar.

## Prerequisites:

You have to chage line 21 in the python code with your /PATH_TO_FILE/token.json

You need to install some libraries:

```
python3 -m pip install google-api-python-client
python3 -m pip install oauth2client
```

You may also need to make the script executable using:

`chmod +x gcalendar.py`

## Usage:

Add these lines to your i3blocks.conf.
```
[gcalendar]
command=/PATH_TO_SCRIPT_AND_TOKEN/gcalendar.py token.json
label=
interval=3600
```
