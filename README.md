# gbf_raid_bot

This script is used to automate GBF raids by making use of Viramate and saved mouse positions. A Twitter consumer key, consumer secret,
an access token, and an access token secret are required. Make sure to save these keys and to set the search keyword before running the script.

## Prerequisite
The program is built using Python 3.X. It needs the Viramate extension installed on your Chrome browser and the following libraries:
- tweepy
- pyperclip
- numpy
- pyautogui

## Description
The program saves coordinates based on the user's mouse coordinates. You only need to save the coordinates once, and it's recommended to 
place the mouse in each element's middle. It'll save the coordinates to a file, but requires it to be loaded each time the program is run. The bot uses Twitter's Streaming API to catch the newest tweet corresponding to the search keyword. It identifies a string of 8 alphanumeric characters (the raid ID) and copies it. The program will open Viramate, which will automatically enter the copied ID into its wordbox, and click the JOIN button.

There will be two checkpoints: if the user can't enter the summon page after clicking the JOIN button and if the user can't enter the
raid after clicking the CONFIRM PARTY button. If the user is unable to enter either pages, the program will continue to search Twitter. 

Otherwise, the program will automatically select the desired element and friend summon, and load the raid screen. The program will randomly
adjust the mouse placements for clicking the summons and CONFIRM PARTY button. After loading the battle, it'll activate 
a skill to ensure that you get loot. Viramate's skill button directly triggers the skills of the character so there is no need to
randomize the mouse positioning and clicks for it. There is a maximum count of 99 runs, but the user can delete the ```maximum_runs```
variable if anything.

## How to Use
- Start the program
- Save coordinates by following the prompt's instructions (only have to do this once).
- Load the coordinate
- Choose the desired raid
- Run the bot

## Notes to keep in mind
- Having a sufficient amount of BP before starting
- When saving coordinates, aim for the middle of the element

## Common Issues

```AttributeError: 'NoneType' object has no attribute 'strip'```

Refer to this [link](https://github.com/tweepy/tweepy/issues/576)

```Status 420: Rate Limit being exceeded.```

User will have to wait it out.
