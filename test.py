from twython import TwythonStreamer
import csv

# Filter out unwanted data
def process_tweet(tweet):
    d = {}
    d['hashtags'] = [hashtag['text'] for hashtag in tweet['entities']['hashtags']]
    d['text'] = tweet['text']
    d['user'] = tweet['user']['screen_name']
    d['user_loc'] = tweet['user']['location']
    return d
    
    
# Create a class that inherits TwythonStreamer
class MyStreamer(TwythonStreamer):     
    # Save each tweet to csv file
    def save_to_csv(self, tweet):
        with open(r'saved_tweets.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow(list(tweet.values()))

    # Received data
    def on_success(self, data):

        # Only collect tweets in English
        if data['lang'] == 'en':
            tweet_data = process_tweet(data)
            self.save_to_csv(tweet_data)

    # Problem with the API
    def on_error(self, status_code, data):
        print(status_code, data)
        self.disconnect()

# Instantiate from our streaming class
stream = MyStreamer('fXm25dDhm1RQOGlyJw5BWMF2b', 'dg4ItiNRQ5JWQBIujENA4yjZQzSyuevyuqi2ePpatVP5PmsC7W', 
                    '743785736814604290-oQCACzR5YwsReElpZFHi4vG6bhYaH7c', '5eE5PdOZSt3wUzx3FvMGUTwmkO1sQOYII2EGtGU9ZBk1t')
# Start the stream
# locations='-74,40,-73,41' '-2,6,1,7'
stream.statuses.filter(locations='-74,40,-73,41')