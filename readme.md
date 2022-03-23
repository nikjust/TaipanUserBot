# Taipan - Userbot for telegram written in pyrogram
# Getting started

## Configuring

1. Create config.py file
2. Configure it by template like this:
``` python
"Taipan config file"

api_hash = "Your api hash"
api_id = "Your api id"
session_name = "Any name for this session"
```
3. Create app on https://my.telegram.org/apps website
4. Copy your `api_hash` and `api_id`
5. Set any ASCII symbols session name
6. Run `main.py`
7. Write your phone number in console
8. Copy verification code from telegram and paste it to console

# Commands and placeholders
## Commands
### reaction
**Send anime reaction gif**

Usage: ` ;reaction {reaction}`

### now
**insert now time and date**

Usage: `{{now}}`

### now:time
**inserts now time**

Usage: `{{now:time}}`

### now:date
**inserts now date**

Usage: `{{now:date}}`

### random
**inserts random number**

Usage: `{{random:[from]:[to]}}`

### google
**Google any query**

Usage: `;google [query] lang={lang}`

### help
**Send this text**

Usage: `;help`