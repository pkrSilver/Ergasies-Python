import tweepy

consumer_key = "x"
consumer_secret = "x"
token = "x"
token_secret = "x"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(token, token_secret)

api = tweepy.API(auth)
handle = input("Input Username: @")

tweets = api.user_timeline(screen_name = handle, count = 10, include_rts = True)
words = ""
wordsList = []

for info in tweets:
    print(info.created_at)
    print(info.text + "\n")
    words = info.text.split()
    wordsList += words

wordLength = [""] * len(wordsList)

for x in range(0, len(wordsList)):
    wordLength[x] = len(wordsList[x])

for i in range(len(wordsList)):
    for j in range(0, len(wordsList)-i-1):
        if wordLength[j] < wordLength[j+1]:
            wordLength[j], wordLength[j+1] = wordLength[j+1], wordLength[j]
            wordsList[j], wordsList[j+1] = wordsList[j+1], wordsList[j]

i = 0
counter = 0
print("Longest Words:")
while counter <= 5:
    if ("http" not in wordsList[i]) and ("@" not in wordsList[i]) and ("RT" not in wordsList[i]):
        print(wordsList[i])
        counter += 1
    i += 1

i = len(wordsList)-1
counter = 0
print("\nShortest Words:")
while counter <= 5:
    if ("http" not in wordsList[i]) and ("@" not in wordsList[i]) and ("RT" not in wordsList[i]):
        print(wordsList[i])
        counter += 1
    i -= 1
