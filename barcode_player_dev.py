prompt = ("Scan a barcode to play some music")
prompt += ("\nor type to quit ")
playing = []
played = []

barcode = input(prompt)
while barcode != 'quit':
    barcode = [int(i) for i in str(barcode)]

    while barcode:
        playing = barcode.pop()
        print("Now playing" + str(playing))
        played.append(playing)

    print("\nWe finished playing that barcode!")
    barcode = input(prompt)
