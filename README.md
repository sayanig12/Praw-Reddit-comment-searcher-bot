# Praw-Reddit-comment-searcher-bot
A script to return comments and authors related to a specific search term
By Sayani Ghosh

1. Open command line
2. Type pip install praw
3. Go to reddit api (https://www.reddit.com/prefs/apps) and create an app. 
   Select the 'script option' and in the redirect uri box, put in: http://localhost:8080. 
   Make a note of the personal use script and secret IDs.
4. Clone repositiory and fill in your details in the praw.ini file.
5. Run from command line.

NB: Code is based on project by https://github.com/elebumm/AlotRedditApi/blob/master/main.py
    Modifications: - Having a .ini file for api_key and also showing the actual comment text along with the author name.
