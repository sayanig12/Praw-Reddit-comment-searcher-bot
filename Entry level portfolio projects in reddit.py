import praw
import re
import time

#log in with reddit credentials
#username = ""
#password = ""

reddit = praw.Reddit()
words_to_match = [r"\bpython\b"]
#words_to_match = [['entry'], ['level'], ['portfolio']]
#words_to_match = ['|'.join(x) for x in words_to_match] #join the words to form phrase to search 
#pattern = r'\b ({}) \s+ ({}) \b'.format(*words_to_match)
#p = re.compile(pattern, re.IGNORECASE) #compiling the pattern to search for aka the grouping of words

results= [] #the list of subreddit links that are returned


def run_bot():
	subreddit = reddit.subreddit('all') #get all subreddits for searching
	print('Accessing data')
	comments = subreddit.comments(limit=100) #accessing the comments on all subreddits
	print('Grabbing comments')
	for comment in comments:
		comment_text = comment.body.lower()
		isMatching = any(re.search(string,comment_text) for string in words_to_match)
		if comment.id not in results and isMatching and comment.author not in results:
			print("Match found. Storing username: " + str(comment.author) + "into list")
			results.append((comment.author, comment_text))

	print("There are currently:" + str(len(results)) + "comments with the words python")
	for item in results:
		print(item)

while True:
	run_bot()
	time.sleep(2)
