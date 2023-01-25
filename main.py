import os
from time import sleep
import keyboard
x = input("Welcome to Text-Based Platformer Project! When you press 'X', your character becomes immune to obstacles represented by the letter 'ı'. Your goal is to earn as much points as you can. Good luck! To start, press enter.")
gameContinues = True
sky = """
    ☁☁ ☀ ☁
    
    """
points = 0
delay = 0.9
while gameContinues:
    text = "o__________"
    char = "o"
    charRestorer = 0
    points += 10
    delay -= 0.05
    for i in range(1,12):
        if charRestorer == 1: charRestorer += 1
        elif charRestorer == 2:
            charRestorer = 3
            char = "o"
        elif charRestorer == 3: charRestorer = 4
        elif charRestorer == 4: charRestorer = 0
        os.system("cls")
        if keyboard.is_pressed("X") and (charRestorer == 0):
            char = "X"
            charRestorer = 1
        text = char + "__________"
        text_l = list(text)
        text_l[-1 * i] = "ı"
        if(text_l[0] == "ı"):
            text_l[0] = "X"
        text = "".join(map(str, text_l))
        print(sky + text + f" | Points : {points}")
        if("oı" in text):
            os.system("cls")
            print("GAME OVER!!! ")
            gameContinues = False
            break
        sleep(delay)
