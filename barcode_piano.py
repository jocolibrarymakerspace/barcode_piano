#!/usr/bin/env python

#We start by defining the opening prompt to the audience
prompt = ("Scan a barcode to play some music")
prompt += ("\nor type quit to quit ")

#We define variables to process the input from the barcode scanner
playing = []
played = []

#We define a variable to store the unprocessed input from the barcode
#and we hook it up to the input prompt.
barcode = input(prompt)

#If the user types "quit", we exit the program

#If the user input is not "quit", we start to process the scanned barcode!
while barcode != 'quit':

    #We break down the contents of barcode into a list of numbers
    barcode = [int(i) for i in str(barcode)]

    #While there are numbers in the barcode list...
    while barcode:

        #We move the latest number in barcode to the playing variable
        playing = barcode.pop()

        #We print out the number in the playing variable...
        print("Now playing" + str(playing))

        #...and finally move that number to the played variable.
        played.append(playing)

    #Once the barcode list is empty, we ask for another barcode to scan
    print("\nWe finished playing that barcode!")
    barcode = input(prompt)
