'''This script is used to automate GBF raids by making use of Viramate and saved mouse positions. A Twitter consumer key, consumer secret,
an access token, and an access token secret are required. Make sure to save these keys and to set the search keyword before running the script.'''
 
from TwitterSearch import *
import re
import pyperclip
import random
import pyautogui
import time
import numpy as np

class GBF():
    def __init__(self):
        self.consumer_key = 'enter_your_consumer_key_here'
        self.consumer_secret = 'enter_your_consumer_secret_here'        
        self.access_token = 'enter_token_here'
        self.access_token_secret = 'enter_token_secret_here'
    
    def go_on_twitter(self):
        try:
            tso = TwitterSearchOrder()
            tso.set_keywords(['enter_raid_search_term_here']) # Example 'Lv100 黒麒麟'
            tso.set_include_entities(False)
            
            ts = TwitterSearch(self.consumer_key, 
                               self.consumer_secret,
                               self.access_token,
                               self.access_token_secret
                               )
                                           
            print('Getting raid ID...\n')                   
            for tweet in ts.search_tweets_iterable(tso):           
                raid = tweet['text']
                break # Get first new tweet
            return raid
            
        except TwitterSearchException as e:
            if e.code == 429:    
                print('Oops. Spammed twitter too much. Will retry in 5minutes')
                cou1 = mouse_positions()
                cou1.countdown(300)
                raid = ''               
            else:
                print('Exception: %i ~ %s' % (e.code, e.message))
                raid = ''
            return raid
        
    def regex_id(self, raid):
        text = re.compile(r'[A-Za-z0-9]{8}')
        text_search = text.search(raid)
        raid_id = text_search.group()
        print('Found raid ID: ', raid_id)
        return raid_id
    
    def checker(self, raid_id):
        old_copy = pyperclip.paste()
        print('Seeing if', '"',old_copy,'"','matches', raid_id)
        if (old_copy != raid_id and len(raid_id) == 8) or old_copy == '':
            pyperclip.copy(raid_id)
            print('New raid id recognized. Beginning automatic clicks...\n')
            return True
        else:
            print('The last raid\'s ID matches the new one copied.')
            print('Will wait 35 seconds before rechecking Twitter.\n')
            cou = mouse_positions()
            cou.countdown(35)
            return False
       
class mouse_positions():
    def countdown(self, count):
        while count >= 0:         
            print(count)
            count -= 1
            time.sleep(1)
  
    def icon(self):
        print('\nPlease hover the mouse to Viramate Icon.')
        self.countdown(5)
        print('Saving position.')
        iconX, iconY = pyautogui.position()
        return iconX, iconY
        print('Saved location.')
        time.sleep(2)
    
    def join(self):
        print('\nHover the mouse to the join button.')
        self.countdown(5)
        print('Saving position.')
        joinX, joinY = pyautogui.position()
        return joinX, joinY
        print('Saved location.')
        time.sleep(2)
    
    def party_screen(self):
        print('\Hover the mouse to the blank space before the "Choose a Summon" text.')
        print('This is used to stop running if can\'t enter the ID.')
        time.sleep(3)
        self.countdown(5)
        print('Saving position.')
        parX, parY = pyautogui.position()
        pr = pyautogui.screenshot().getpixel((parX, parY))
        return parX, parY, pr
        print('Saved location.')
        time.sleep(2)
    
    def summon(self):
        print('\nHover the mouse to the Element\n')
        self.countdown(5)
        print('Saving position...')
        elementX, elementY = pyautogui.position()
        print('Saved.')
        time.sleep(2)
        print('Hover the mouse to the actual summon.')
        self.countdown(5)
        print('Saving summon position...')
        summonX, summonY = pyautogui.position()
        return elementX, elementY, summonX, summonY
        print('Saved location.')
        time.sleep(2)
    
    def confirm_button(self):
        print('\nHover the mouse to the Confirm party button.')
        self.countdown(5)
        print('Saving position...')
        confirmX, confirmY = pyautogui.position()
        return confirmX, confirmY
        print('Saved location.')
        time.sleep(2)
    
    def attack(self):
        # Viramate skill bottom click, so no need for portrait->skill
        print('\nHover the mouse to the skill button UNDER the portrait.')
        self.countdown(13)
        skillbuttonX, skillbuttonY = pyautogui.position()
        print('\nHover the mouse to the green section of the Heal button.')
        self.countdown(4)
        print('Saving position...')
        recogX, recogY = pyautogui.position()
        im = pyautogui.screenshot().getpixel((recogX, recogY))
        print('Saved location.\n')
        return skillbuttonX, skillbuttonY, recogX, recogY, im
       
class bot():   
    def save_coordinates(self): 
        sc = input('Press Enter to begin. Type anything else to exit.\n>>> ')
        if sc == "":
            mouse = mouse_positions()
            iconX, iconY = mouse.icon()
            joinX, joinY = mouse.join()
            parX, parY, pr = mouse.party_screen()
            elementX, elementY, summonX, summonY = mouse.summon()
            confirmX, confirmY = mouse.confirm_button()
            skillbuttonX, skillbuttonY, recogX, recogY, im = mouse.attack()
            np_xy = np.array([
            [iconX, joinX, elementX, summonX, confirmX, skillbuttonX, recogX, parX],
                             [iconY, joinY, elementY, summonY, confirmY, skillbuttonY, recogY, parY]]
                             )
            np_im = np.array(im)
            np_pr = np.array(pr)
            np.savetxt("np_xy_coords.txt", np_xy)
            np.savetxt("np_im_coords.txt", np_im)
            np.savetxt("np_pr_coords.txt", np_pr)
            print('Completed saving all coordinates.\n')
        else:
            pass
    
    def load_coordinates(self):
        try:
            xy = np.loadtxt('np_xy_coords.txt')
            npim = np.loadtxt('np_im_coords.txt')
            nppr = np.loadtxt('np_pr_coords.txt')
            print('Loaded coordinates.\n')
            return xy, npim, nppr
        except:
            print('Could not find any coordinate files. Are you sure you saved?')
            print('Please try again.')
            
    def vira_clicks(self, xy, npim, nppr, counter):
            print('Press CTRL+C to exit.')
            print('Starting...\n')
            print('Hovering to Vira icon...')
            pyautogui.click(xy[0,0], xy[1,0]) #Vira button
            time.sleep(1)
            print('Joining...')
            pyautogui.click(xy[0,1], xy[1,1]) #Join button
            time.sleep(5)
            if pyautogui.pixelMatchesColor(xy[0,7], xy[1,7], nppr) == True:
                print('Clicking Element...')
                pyautogui.click(xy[0,2], xy[1,2]) # Element
                time.sleep(2)
                print('Clicking Summon...')
                pyautogui.moveTo((xy[0,3], xy[1,3]))
                pyautogui.moveRel(random.randrange(0,225),random.randrange(0,25))
                pyautogui.click()
                time.sleep(2)
                print('Clicking the Confirm Party button...')
                pyautogui.moveTo((xy[0,4], xy[1,4]))
                pyautogui.moveRel(random.randrange(0,50), None)
                pyautogui.click()
                print('Waiting...')
                time.sleep(13)
                print('Did we join the raid?\n')
                # If the heal button is recognized, then run the bot
                if pyautogui.pixelMatchesColor(xy[0,6], xy[1,6], npim) != True:
                    print('Could not join raid.\n')
                    print('Done.\n')
                else:
                    pyautogui.moveTo(xy[0,5], xy[1,5])
                    pyautogui.click()
                    counter += 1
                    print('Finished! Counter number remaining: ', counter)
            else:
                print('There was an error in joining the raid.')
                print('Counter number remaining: ', counter,'\n')
            return counter

             
def main():
    print('Make save there are saved coordinates before beginning.\n')
    time.sleep(1)
    while True:
        print('What would you like to do?\n***')
        print('1 - Run Bot\n2 - Save new coordinates\n3 - Load coordinates\nq - Exit\n***\n')
        app = bot()
        answer = input('>> ')   
        if answer == "1":
            counter = 0
            while counter < 6:
                try:
                    gb = GBF()
                    raid_id = gb.regex_id(gb.go_on_twitter())
                    status = gb.checker(raid_id)
                    if status == True:
                        app.vira_clicks(xy, npim, nppr, counter)
                    elif status == False:
                        print('Rechecking Twitter...\n')
                    else:
                        print('None type found.')
                except KeyboardInterrupt:
                    print('Stopping the bot...\n')
                    break
            print('Done for now.\n')
        elif answer == "2":
            app.save_coordinates()
        elif answer == "3":
            xy, npim, nppr = app.load_coordinates()
        elif answer.lower() == "q":
            print('Exiting...\n')
            break
        else:
            print('Unknown command. Please try again.\n')

if __name__ == "__main__":
    main()
            
        
    
