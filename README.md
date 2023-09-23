# google-analytics-discord-bot
Discord Bot that can pull valuable data from Google Analytics that has been incorporated in the front-end of any web app.

# Setup

### Google Analytics API ###

Follow steps 1 and 2 from:
https://developers.google.com/analytics/devguides/reporting/data/v1/quickstart-client-libraries

![image](https://github.com/pvico12/google-analytics-discord-bot/assets/73671546/c756d7cb-f92e-46a6-a126-ae6fe3e51948)

**Put the credential JSON in the *root* directory of this repo.**

Declare the JSON credentials filename as a global constant.

```
export DISCORD_TOKEN="<your-discord-bot-token>"
```



### Discord Bot Token

Create a bot, and add it's token as a global environment variable:

```
export GOOGLE_ANALYTICS_API_KEY_JSON_FILE="<google-analytics-credential-json-file-name>"
```


### Install Python Packages

Install the following packages with ```pip```

```
pip install google-analytics-data
pip install discord
pip install python-dotenv
pip install table2ascii
```


### Python virtual environment

Create your python virtual environment. You can choose any ```<env-name>``` you wish.

```
python3 -m venv <env-name>
```


# Deploy

Once you have completed the setup, activate your python virtual environment with

```
source <env-name>/bin/activate
```

Now, run the bot

```
python3 bot.py
```

