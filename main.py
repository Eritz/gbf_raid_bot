import tweepy
import pyperclip
import json
import re
import time
import threading
from bot import MousePositions, Bot
from raidnames import options, choose_a_raid

class RaidListener(tweepy.StreamListener):
    def __init__(self):
        self.stop_this = []
    
    def on_error(self, status):
        print('Status is: ', status)
        if status == 420:
            print('Being rate limited.')
            return False
        elif status == 406:
            print('Invalid format is specified in the request')
            return False
    
    def on_data(self, data):
        if len(self.stop_this) >= 1:
            return False
        else:
            tweet_json = json.loads(data) # Converts to a Python dictionary
            tweet = tweet_json['text'] #Get the text from json dictionary
            self.extract(tweet)          
            return True
   
    def extract(self, result):
        try:
            keywords = re.compile('[A-Za-z0-9]{8}')
            text_search = keywords.search(result)
            raid_id = text_search.group() #Uncomment below to see output in console
            #print('Found raid ID: {}...\nNow copying...\n'.format(raid_id))
            pyperclip.copy(raid_id)
            #print('Finished copying ({})\n'.format(raid_id))
        except:
            return False
    
    def disconnect(self):
        self.stop_this.append('stop')

            
class RaidStream(RaidListener):
    def __init__(self):
        self.consumer_key = 'your consumer key here'
        self.consumer_secret = 'your consumer secret here'        
        self.access_token = 'your token here'
        self.access_token_secret = 'your token secret here'
    
    def twitter_login(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.secure = True
        auth.set_access_token(self.access_token, self.access_token_secret)
        api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify=True)
        return api       
    
    def twitter_results(self, api, RaidListener, search):
        stream = tweepy.Stream(auth = api.auth, listener = RaidListener)
        stream.filter(track=[search], async=True)
            
def checker(raid_old):
    check_this = pyperclip.paste()
    if check_this == '' or check_this == raid_old:
        return raid_old, False
    elif len(check_this) == 8 and check_this != raid_old: 
        print('New raid id recognized. Beginning automatic clicks...\n')
        raid_old = check_this
        return raid_old, True
    else: # Pasting something different outside GBF
        return raid_old, False
            
def main():
    print('Make save there are saved coordinates and a search term set before beginning.\n')
    time.sleep(2)
    search = ''
    while True:
        print('What would you like to do?\n***')
        print('1 - Run Bot\n2 - Save new coordinates\n3 - Load coordinates\n4 - Twitter Search Term\nq - Exit\n***\n')
        app = Bot()
        gbf = RaidListener()
        stream = RaidStream()
        answer = input('>> ')   
        if answer == "1":
            print('Starting...')
            thread = threading.Thread(target=stream.twitter_results, args=(stream.twitter_login(), gbf, search))
            thread.setDaemon(True)
            thread.start() # Automatically copies next tweet
            raid_old = 'nothing'
            maximum_runs = 99
            while maximum_runs > 0:
                try:
                    checked_result, status = checker(raid_old)
                    raid_old = checked_result
                    if status == True:
                        print('Using ID: {} \n'.format(pyperclip.paste()))
                        # Make a new thread that joins with the twitter one
                        thread_click = threading.Thread(target=app.vira_clicks, args=(xy, npim, nppr))
                        thread_click.setDaemon(True)
                        thread_click.start()
                        thread_click.join()
                        maximum_runs -= 1
                        print('Done.\nCurrent maximum runs: {}\n'.format(maximum_runs))
                    elif status == False:
                        pass
                    elif status == None:
                        print('None type found.')                           
                except KeyboardInterrupt: # Catch interrupt for the bot actions
                    maximum_runs = 0
            print('Stopping the bot...\n')
            gbf.disconnect()
            
        elif answer == "2":
            app.save_coordinates()         
        elif answer == "3":
            xy, npim, nppr = app.load_coordinates()     
        elif answer == "4":
            search = choose_a_raid(options)
            print('Twitter search term is set to \"{}\"\n'.format(search))       
        elif answer.lower() == "q":
            print('Exiting...\n')
            break     
        else:
            print('Unknown command. Please try again.\n')

if __name__ == "__main__":
    main()