# YouTube Discord Alert

Send a message to a Discord channel when new videos are posted to a list of YouTube channels.

## Running the App

The app is distributed as the Docker image `ghcr.io/micthiesen/youtube-discord-alert`.

### Using Docker

```bash
docker run \
```

### Using Docker Compose

```yml
yda:
  image: ghcr.io/micthiesen/youtube-discord-alert
  container_name: yda
  restart: unless-stopped
  environment:
    - CHANNEL_IDS=["UCFrZFkoK9-cZf6LtOD0a_uw", "UCqIDB2oovYTOHx1lbMQxjtg"]
    - DISCORD_WEBHOOK=https://discordapp.com/api/webhooks/123/ABC
    - YOUTUBE_API_KEY=CHanGeMe
    - POLL_INTERVAL=300
  volumes:
    - ./volumes/yda:/data
```

### Options / Environment Variables



See the `Settings` class in [src/config.py](https://github.com/micthiesen/youtube-discord-alert/blob/main/src/config.py) for the default values.

## Developing

Requirements:

- Docker
- Python 3.10 and the dev packages: `pip install -r requirements-dev.txt`
- The production packages: `pip install -r requirements.txt` (optional, for code completion)

Copy `.env.local.example` to `.env.local` and replace the `DISCORD_WEBHOOK` and `YOUTUBE_API_KEY` values.

Run `./bin/dev.py` and the app will automatically restart when source files change.
