# WHO.py
> The code in this repository is a Python implementation of the Instaloader library.

Automated script that let you know who of your following users in Instagram do not follow you back.

## Requirements
Be sure to run `pip install -r requirements.txt` on your command line to install the required dependencies.

## Usage
> Progress of followers or following of your account is saved in case you accidentally interrupted your process. You can continue without data losing!.

`python3 who.py` will log in to Instagram via a request to your browser and then start the process of getting all of your followers & followees combining web scrapping with the Instagram API.

## Output
#### `who.txt` List of users that do not follow you back.
#### `whoyes.txt` List of users that follow you back.

#### `username_followers.txt` List of users that follow you.
#### `username_following.txt` List of users that you follow.
