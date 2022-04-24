# Bitly url shorterer

The script generate bitlink url using bitly API. If bit.ly url is given it returns total clicks count for a given link.

### How to install

Registration at [bitly.com](bitly.com) is required. Generate token at API settings page [here](https://app.bitly.com/settings/api/)
Place your token in `.env` file:
```commandline
BITLY_TOKEN = 'here should be your token'
```

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).