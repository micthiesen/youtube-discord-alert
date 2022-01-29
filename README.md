# YouTube Discord Alert

Send a message to a Discord channel when new videos are posted by certain YouTube channels.

## Running the App

The app is distributed as the Docker image `ghcr.io/micthiesen/youtube-discord-alert`.

It's useful to mount a data volume as a history file is maintained to prevent posting the same video more than once to Discord.

To create a Discord webhook, [see here](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks).

To create a YouTube API key, [see here](https://developers.google.com/youtube/registering_an_application). Create an API key for the YouTube Data API.

### Using Docker

```bash
docker run -d \
  --name=yda \
  -e CHANNEL_IDS='["UCFrZFkoK9-cZf6LtOD0a_uw", "UCqIDB2oovYTOHx1lbMQxjtg"]' \
  -e DISCORD_WEBHOOK=https://discordapp.com/api/webhooks/123/ABC \
  -e YOUTUBE_API_KEY=CHanGeMe \
  -v /path/to/data:/data \
  --restart unless-stopped \
  ghcr.io/micthiesen/youtube-discord-alert
```

### Using Docker Compose

```yml
yda:
  image: ghcr.io/micthiesen/youtube-discord-alert
  container_name: yda
  environment:
    - CHANNEL_IDS=["UCFrZFkoK9-cZf6LtOD0a_uw", "UCqIDB2oovYTOHx1lbMQxjtg"]
    - DISCORD_WEBHOOK=https://discordapp.com/api/webhooks/123/ABC
    - YOUTUBE_API_KEY=CHanGeMe
  volumes:
    - /path/to/data:/data
  restart: unless-stopped
```

### Options / Environment Variables

| Environment Variable | Type | Default Value | Required | Explanation |
| -------------------- | ---- | ------------- | -------- | ----------- |
| `LOG_LEVEL` | `DEBUG` \| `INFO` \| `WARNING` \| `ERROR` \| `CRITICAL` \| | `INFO` | No | Detail of logs |
| `POLL_INTERVAL` | Integer | `300` | No | How often to check for new videos, in seconds |
| `CHANNEL_IDS` | List of strings (JSON formatted) | `[]` | No | Channel IDs to monitor |
| `DISCORD_WEBHOOK` | String | N/A | Yes | Discord webhook for a channel |
| `YOUTUBE_API_KEY` | String | N/A | Yes | YouTube API key |
| `LATEST_CHANNEL_VIDEOS_COUNT` | Integer | `10` | No | How many videos to retrieve per channel when polling |
| `MAX_HISTORY_PER_CHANNEL` | Integer | `20` | No | How many videos to keep track of per channel (to prevent duplicate posts). Should always be greater than `LATEST_CHANNEL_VIDEOS_COUNT` |

## Developing

Requirements:

- Docker
- Python 3.10 and the dev packages: `pip install -r requirements-dev.txt`
- The production packages: `pip install -r requirements.txt` (optional, for code completion)

Copy `.env.local.example` to `.env.local` and replace the `DISCORD_WEBHOOK` and `YOUTUBE_API_KEY` values.

Run `./bin/dev.py` and the app will automatically restart when source files change.
