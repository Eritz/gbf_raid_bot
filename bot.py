import time
import pyautogui
import random
import numpy as np

class MousePositions():
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

class Bot():   
    def save_coordinates(self): 
        sc = input('Press Enter to begin. Type anything else to exit.\n>>> ')
        if sc == "":
            mouse = MousePositions()
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
            
    def vira_clicks(self, xy, npim, nppr):
            try:
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
                    else:
                        pyautogui.moveTo(xy[0,5], xy[1,5])
                        pyautogui.click()
                        time.sleep(5)
                else:
                    print('There was an error in joining the raid.')
            except KeyboardInterrupt:
                return False
            except: #WinError 5 bypass
                pass

