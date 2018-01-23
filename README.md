# What is this?
A long requested feature at /r/livecounting (LC) is a way to track the number of counts a counter preforms without needing to wait for the daily Hall of Counters (HoC). This is a hopefully simple method to do just that. This has been created with Windows OS in mind but it is possible to modify for use with other operating systems.

# What you need to use
1. Reddit Account
2. Be a part of this [counting thread](https://www.reddit.com/live/ta535s1hq2je/)
3. [Python 3](https://www.python.org/ftp/python/3.6.4/python-3.6.4.exe)
4. Websocket - [Learn how to install](https://github.com/artbn/count_counter#how-to-install-websocket)
5. PRAW - [Learn how to install](https://github.com/artbn/count_counter#how-to-install-websocket-1)

## How to install Websocket
1. Open CMD (Ctrl + R and then type in `cmd`)
2. type `pip install websocket-client` and hit enter

## How to install PRAW
1. Open CMD (Ctrl + R and then type in `cmd`)
2. type `pip install praw` and hit enter

# Set up

Once you have everything you need, move on to this section.

## Download the code

1. Click the green button titled `clone or download` on this page
2. Select `download as Zip` from the drop down menu
3. Unzip and save the folder to any location

## Set up a reddit bot
In order for the tracker to work, it must be allowed by reddit. Do so, follow these instructions.

1. Sign in to your reddit account
2. Click `prefrences` on the upper right corner
3. Click `apps` on the top menu
4. Scroll down and click on the `create another app...` button
5. Enter `counts_counter` in name
6. Select `script` from the radio buttons
7. Enter `http://localhost:8080` in the redirict uri
8. Click `create app`
9. Keep this page open and move to the next section

## Add info to config.py

1. Open `config.py` in the folder that you downloaded
2. You should find something like this:
```
# Enter your reddit username & password
username = "_"
password = "_"

# Get this from reddit preferences/apps
client_id = "_"
client_secret = "_"

# Change this to track counts in another thread
thread = "ta535s1hq2je"
```
3. Replace the `_` with your reddit username and password (don't worry, this is only saved locally on your computer). Keep the quotation marks.
4. From the reddit page where you created the script, copy the client ID (located under personal use script). Should be a random bunch of letters and numbers. Replace the `_` with this
5. Copy the secret on the same page and replace the appropriate `_`.
6. Save and close `config.py`

Remember to keep your client id/client secret both secret just as you would for your username/password.

## Running the tracker

1. Open the folder you downloaded again
2. Double click on `run.bat` to run the tracker
3. A `cmd` screen should pop up. It should take a moment to log in and then begin tracking your counts.
4. As you count, it will display the current number of counts that you have counted.
5. When you are done using it, just close the screen. The count will reset when you restart it again.

# Disclaimer
Testing for this has been minimal. If it doesn't work as expected for you, contact /u/artbn. Also contact me if the instructions above are unclear.