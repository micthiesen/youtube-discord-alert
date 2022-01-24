# YouTube Discord Alert

Send a message to a Discord channel when new videos are posted to a list of YouTube channels.

## Running the App

The app can be deployed using Docker: `docker build -t youtube-discord-alert . && docker run --rm youtube-discord-alert`

## Developing

Requirements:

- Docker
- Python 3.10 and the dev packages: `pip install -r requirements-dev.txt`

Run `./bin/dev.py` and the app will automatically restart when source files change.
