#!/usr/bin/env python

#Barcode piano player
#Based on a request from Alice Bernard on the Labenbib Facebook group - https://www.facebook.com/groups/fablabbib/

#This script has been tested on a Raspberry Pi 3 scomputer with:
#- Raspbian Stretch
#- Python (2 or 3) - https://www.python.org/
#- VLC - https://www.videolan.org/vlc/
#- Python-VLC bindings - https://wiki.videolan.org/Python_bindings 
#- Free piano keys samples from the Piano Notes 1 Octave from pinkyfinger on Freesound.org - https://freesound.org/people/pinkyfinger/packs/4409/

#Upcoming tutorial at https://www.instructables.com/member/jocomakerspace/

#How to use
#Turn on Raspberry pi and download script
#Copy sounds to the same folder as your script
#Add the complete path to the sounds to your playlist list

#The party starts below this line!

#We import the time module
import time

#We import the VLC module
import vlc

#We start by defining the opening prompt to the audience
prompt = ("Scan a barcode to play some music")
prompt += ("\nor type quit to quit ")

#We define lists to process the input from the barcode scanner
playing = []
played = []

#We define a list to store the path to the sounds on your Raspberry Pi
playlist = ['/01.wav/', '/02.wav/', '/03.wav/', '/04.wav/', '/05.wav/', '/06.wav/', '/07.wav/', '/08.wav/', '/09.wav/', '/10.wav/'] 

while True:

    #We define a variable to store the input from the barcode scanner
    #and we hook it up to the input prompt.
    barcode = input(prompt)

    #If the user input is "quit", we leave the program
    if barcode == quit:
        break

    #If the user scans a barcode, we start processing the input
    else:
        #We break down the contents of barcode into numbers and store them in a list
        barcode = [int(i) for i in str(barcode)]

        #As long as there are numbers in the barcode list...
        while barcode:

            #We move the latest number in the list to the playing variable
            playing = barcode.pop()

            #We print out the number in the playing variable...
            print("Now playing" + str(playing))

            #We setup VLC to play the file in the list corresponding with the number currently processed
            player = vlc.MediaPlayer(playlist[playing])

            #We catch a little break to let any previous sounds finish playing
            time.sleep(0.35)

            #We play the VLC track we loaded earlier...
            player.play()

            #...and finally move that number to the played variable.
            played.append(playing)

        #Once the barcode list is empty, we let the user know - and start all over again!
        print("\nWe finished playing that barcode!")
