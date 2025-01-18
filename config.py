import os
import sys
import json

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.json")


if not os.path.exists(CONFIG_PATH):
    print(f'{CONFIG_PATH} not found')
    sys.exit(1)


configdata = json.load(open(CONFIG_PATH, 'r'))

ALLOWED_USER_NAMES = configdata['ALLOWED_USER_NAMES']
OPENAI_API_KEY = configdata.get('OPENAI_API_KEY', None)

TELEGRAM_TOKEN = configdata['TELEGRAM_TOKEN']

REPLICATE_API_KEY = configdata.get('REPLICATE_API_KEY', None)

ANTHROPIC_API_KEY = configdata.get('ANTHROPIC_API_KEY', None)

YT_DL_DIR = configdata.get('YT_DL_DIR', None)
YT_DL_URL = configdata.get('YT_DL_URL', None)
SCHEDULES = configdata.get('SCHEDULES', None)
{
    "ALLOWED_USER_NAMES": ["stale_breads"],
    "OPENAI_API_KEY": "****",
    "TELEGRAM_TOKEN": "6966957722:AAGPCG3KKljignhOns8MP4XcgatVaalpXIc",
    "ANTHROPIC_API_KEY": "****",
    "REPLICATE_API_KEY": "",
    "YT_DL_DIR": "/var/data/uploads",
    "YT_DL_URL": "https://somehost.com/uploads",
    "SCHEDULES": 1
}
