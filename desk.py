from appscript import app, mactypes
from time import sleep
import random
import re
import subprocess
from math import ceil
from datetime import datetime
from datetime import date
from PIL import Image, ImageDraw, ImageFont

def get_speaker_output_volume():
    """
    Get the current speaker output volume from 0 to 100.

    Note that the speakers can have a non-zero volume but be muted, in which
    case we return 0 for simplicity.

    Note: Only runs on macOS.
    """
    cmd = "osascript -e 'get volume settings'"
    process = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True)
    output = process.stdout.strip().decode('ascii')

    pattern = re.compile(r"output volume:(\d+), input volume:(\d+), "
                         r"alert volume:(\d+), output muted:(true|false)")
    volume, _, _, muted = pattern.match(output).groups()

    volume = int(volume)
    muted = (muted == 'true')

    return 0 if muted else volume

bList = ["sunset", "blocks", "soundwave", "eye", "cat", "equalizer", "kahoot", "cyber", "lsd", "blackcat", "banana", "fake", "placeholder-eq", "city", "city2", "trainview", "ring", "unicorn", "floatingisland", "city3", "atoms", "lsd2", "abstract", "stormtrooper", "icanfly", "brokenpatrick", "evolution", "northernlights", "volcano"]
bListType = ["interactive", "interactive", "interactive", "animated", "animated", "static", "animated", "static", "animated", "animated", "animated", "static", "sound-triggered",  "animated", "animated", "animated", "interactive", "animated", "animated", "animated", "animated", "animated", "static", "static", "static", "static", "static", "time", "date"]
bListSpeed = [0, 0, 0, 90, 90, 0, 85, 0, 100, 90, 95, 0, 0, 90, 90, 90, 0, 97, 90, 90, 90, 100, 0, 0, 0, 0, 0, 0, 0]
print("------")
print("All Desktop Backgrounds")
print("----")
for b in sorted(bList):
    print(b + " - " + bListType[bList.index(b)])
while True:
    backdrop = input("Which backdrop would you like? ")
    if backdrop in bList:
        break
    else:
        print("Um... choose a valid background...")
print("------")

if bListType[bList.index(backdrop)] == "animated":
    while True:
        try:
            print(f"Recommended speed: {bListSpeed[bList.index(backdrop)]}")
            speed = input("Choose speed (integer) from 1 to 100: ")
            if int(speed) > 0 and int(speed) < 101:
                speed = 1 - (0.0099 * (int(speed)))
                break
            else:
                print("Please use a valid speed (integer from 1 to 100).")
        except:
            print("Please use a valid speed (integer from 1 to 100).")
    print("------")

if bListType[bList.index(backdrop)] != "static":
    print("Use ctrl-c to finish (animations and interactions will become static).")
    print("------")

if bListType[bList.index(backdrop)] == "interactive":
    while True:
        if backdrop == "soundwave" or backdrop == "sunset":
            backdropNum = ceil(get_speaker_output_volume()/25)
        elif backdrop == "blocks":
            backdropNum = ceil(get_speaker_output_volume()/10)
        elif backdrop == "ring":
            backdropNum = ceil(get_speaker_output_volume()/17)
        app('Finder').desktop_picture.set(mactypes.File(f'img/{backdrop}{backdropNum}.jpg'))
elif bListType[bList.index(backdrop)] == "animated":
    backdropNum = 0
    bN = 0
    if backdrop == "lsd" or backdrop == "lsd2":
        app('Finder').desktop_picture.set(mactypes.File('img/photosensitivitywarning.jpg'))
        sleep(5)
    while True:
        if backdrop == "eye":
            backdropNum += 1
            backdropNum = backdropNum % 8  
        elif backdrop == "cat":
            backdropNum += 1
            backdropNum = backdropNum % 6
        elif backdrop == "kahoot" or backdrop == "kahootFrame":
            backdrop == "kahootFrame"
            backdropNum += 1
            backdropNum = backdropNum % 7
        elif backdrop == "lsd" or backdrop == "0":
            backdrop = "0"
            if bN < 9:
                bN += 1
                backdropNum = "00" + str(bN)
            elif bN < 99:
                bN += 1
                backdropNum = "0" + str(bN)
            elif bN < 399:
                bN += 1
                backdropNum = str(bN)
            else:
                bN = 0
        elif backdrop == "blackcat" or backdrop == "8998adc40112985a8f29cf414925d390-":
            backdrop = "8998adc40112985a8f29cf414925d390-"
            backdropNum = backdropNum % 110 + 1
        elif backdrop == "banana" or backdrop == "tenor-":
            backdrop = "tenor-"
            backdropNum += 1
            backdropNum = backdropNum % 9
        elif backdrop == "city" or backdrop == "3cab434622d9fabfde2f46e9a51380d6-":
            backdrop = "3cab434622d9fabfde2f46e9a51380d6-"
            backdropNum += 1
            backdropNum = backdropNum % 36
        elif backdrop == "city2" or backdrop == "ae78df1ec46fe622dd0d3de6907fbe74-":
            backdrop = "ae78df1ec46fe622dd0d3de6907fbe74-"
            backdropNum += 1
            backdropNum = backdropNum % 64
        elif backdrop == "trainview" or backdrop == "tumblr_f3aa6e82e1dbf5b598f17f7252438b11_5f4b51db_500-":
            backdrop = "tumblr_f3aa6e82e1dbf5b598f17f7252438b11_5f4b51db_500-"
            backdropNum += 1
            backdropNum = backdropNum % 8
        elif backdrop == "unicorn" or backdrop == "1920x1080-Wallpaper-Gifs-Keysinspectorinc.com-":
            backdrop = "1920x1080-Wallpaper-Gifs-Keysinspectorinc.com-"
            backdropNum += 1
            backdropNum = backdropNum % 67
        elif backdrop == "floatingisland" or backdrop == "floatingisland-":
            backdrop = "floatingisland-"
            backdropNum += 1
            backdropNum = backdropNum % 300
        elif backdrop == "city3" or backdrop == "d733b491c5031518eed0e59a49511c9a-":
            backdrop = "d733b491c5031518eed0e59a49511c9a-"
            backdropNum += 1
            backdropNum = backdropNum % 72
        elif backdrop == "atoms" or backdrop == "ShorttermGiantGuillemot-small-":
            backdrop = "ShorttermGiantGuillemot-small-"
            backdropNum += 1
            backdropNum = backdropNum % 88
        elif backdrop == "lsd2" or backdrop == "giphy-":
            backdrop = "giphy-"
            backdropNum += 1
            backdropNum = backdropNum % 30

        app('Finder').desktop_picture.set(mactypes.File(f'img/{backdrop}{backdropNum}.jpg'))
        sleep(speed)
elif bListType[bList.index(backdrop)] == "time":
    while True:
        now = datetime.now()
        text = now.strftime("%H:%M:%S")
        img = Image.open(f"{backdrop}.jpg")
        draw = ImageDraw.Draw(img)
        # font = ImageFont.truetype(<font-file>, <font-size>)
        fontSize = int(ceil((img.width + img.height)/15))
        font = ImageFont.truetype("comicate.ttf", fontSize)
        # draw.text((x, y),"Sample Text",(r,g,b))
        draw.text((img.width/2 - (len(text)*(fontSize/4)), img.height/2), text,(255, 255, 255),font=font)
        img.save(f'{backdrop}{text}.jpg')
        app('Finder').desktop_picture.set(mactypes.File(f'img/{backdrop}{text}.jpg'))
elif bListType[bList.index(backdrop)] == "date":
    while True:
        text = str(date.today())
        img = Image.open(f"img/{backdrop}.jpg")
        draw = ImageDraw.Draw(img)
        # font = ImageFont.truetype(<font-file>, <font-size>)
        fontSize = int(ceil((img.width + img.height)/15))
        font = ImageFont.truetype("comicate.ttf", fontSize)
        # draw.text((x, y),"Sample Text",(r,g,b))
        draw.text((img.width/2 - (len(text)*(fontSize/4)), img.height/2), text,(255, 255, 255),font=font)
        img.save(f'img/{backdrop}{text}.jpg')
        app('Finder').desktop_picture.set(mactypes.File(f'img/{backdrop}{text}.jpg'))
elif bListType[bList.index(backdrop)] == "static":
    app('Finder').desktop_picture.set(mactypes.File(f'img/{backdrop}.jpg'))
elif bListType[bList.index(backdrop)] == "sound-triggered":
    pass