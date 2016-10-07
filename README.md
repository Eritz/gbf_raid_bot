# gbf_raid_bot

This script is used to automate GBF raids by making use of Viramate and saved mouse positions. A Twitter consumer key, consumer secret,
an access token, and an access token secret are required. Make sure to save these keys and to set the search keyword before running the script.

## Prerequisite
The program is built using Python 3.X. It needs the Viramate extension installed on your Chrome browser and the following libraries:
- TwitterSearch
- pyperclip
- numpy
- pyautogui

## Description
The program saves coordinates based on the user's mouse coordinates. You only need to save the coordinates once, and it's recommended to 
place the mouse in each element's middle. It'll save the coordinates to a file, but requires it to be loaded each time the program is run. The bot
will check Twitter for the first tweet corresponding to the search keyword. It'll identify a string of 8 alphanumeric characters 
and copies it. The program will open Viramate, which will automatically enter the copied ID into its wordbox, and click the JOIN button.

There will be two checkpoints: if the user can't enter the summon page after clicking the JOIN button and if the user can't enter the
raid after clicking the CONFIRM PARTY button. If the user is unable to enter either pages, the program will continue to search Twitter. 

Otherwise, the program will automatically select the desired element and friend summon, and load the raid screen. The program will randomly
adjust the mouse placements for clicking the summons and CONFIRM PARTY button. After loading the battle, it'll activate 
a skill to ensure that you get loot. Viramate's skill button directly triggers the skills of the character so there is no need to
randomize the mouse positioning and clicks for it. After 5 runs, the bot will stop (because of Pending battles). The user can delete the ```counter```
variable if he/she wants the bot to run indefinitely.

##Common Issues

If the last raid ID copied from Twitter reappears in the program's search, then the program will reattempt to 
research Twitter for a new ID. If there is no new raid ID identified, this process will loop and additional queries will be sent.
Eventually, Twitter will stop any queries that are executed, and this can lead to heavy frustration.

The servers might delay. This causes the program to load the page and click incorrectly. The user can tweak the ```time.sleep``` settings
to adjust the program's delays.

