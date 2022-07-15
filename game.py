import cowsay
import sys
from os.path import exists
from collections import Counter
import re
import random
global name
name = ""
version = 1


def main():
    # main does the running
    global name
    name = cow(f"What is your name?\nVersion #{version}", prompt="Name: ")
    if name == "":
        name = "dummy"
    load(name)
    cow(f"So they call you {name} is that so?  Well my name is Cow")
    cow("I'm here to help you on your farming adventure")

    while True:
        pick = cow(
            "You have a few options. You can: \n[1] Sleep\n[2] Open your Bag\n[3] Check stats and crops\n[4] Harvest\n[5] Market (Buy/Sell)\n[6] Save and Quit",
            prompt="Pick a number: ",
        )
        match pick.lower():
            case "1" | "1." | "sleep" | "s":
                cow(
                    "Goodnight Sleep tight.  Don't let any advertures bite in the night!"
                )
                sleep()
            case "2" | "2." | "bag" | "b" | "o" | "open":
                print(get_bag())
            case "3" | "3." | "check" | "stats" | "check stats" | "check crops":
                get_stats()
            case "4" | "4." | "harvest" | "h":
                harvest()
            case "5" | "5." | "market" | "buy" | "sell":
                market()
            case "6" | "6." | "quit" | "q":
                save(name)
                sys.exit()


stats = dict()


def save(name):
    with open(name + ".save", "w") as f:
        for each in stats:
            f.write(f"{each};{stats[each]}\n")
    print("Saving please press enter...")


def load(file):
    # Loads file in the following format
    # str,n
    # max_hp,n
    # hp,n
    # level,n
    # def,n
    # gold,n
    # seed_bag = list()
    # loot_bag = list()
    # feild = ##|
    # feildsize = 1
    file = f"{file}.save"
    if exists(file):
        f = open(file, "r")
        lines = f.readlines()
        for each in lines:
            stat, num = each.split(";")
            stats[stat] = num.replace("\n", "")
    else:
        seed_bag = ["1. 🥔 Seeds"]
        loot_bag = list()
        feild = "##|"

        f = open(file, "w")
        load_stat(f, "str")
        load_stat(f, "max_hp", defualt_n="10")
        load_stat(f, "hp", defualt_n="10")
        load_stat(f, "level")
        load_stat(f, "def")
        load_stat(f, "gold")
        load_stat(f, "seed_bag", defualt_n=seed_bag)
        load_stat(f, "loot_bag", defualt_n=loot_bag)
        load_stat(f, "feild", defualt_n=feild)
        load_stat(f, "feildsize")
        load_stat(f, "exp")
        f.close()


def load_stat(file, stat, defualt_n="1"):
    # loads stats cuz I was to lazy to type each one out 2 times
    file.write(f"{stat};{defualt_n}\n")
    stats[stat] = defualt_n


def get_stats():
    # gets and displays your current stats
    print("_" * 12)
    for key, value in stats.items():
        if key == "feild":
            continue
        if key == "seed_bag":
            print("Seeds: ")
            seed_list=list()
            for each in value:
                seed_list.append(id_to_item(each))
            seed_str = str(Counter(seed_list))
            print(seed_str
        .replace("}", "")
        .replace("'", "")
        .replace("{", "")
        .replace(")", "")
        .replace('"', "")
        .replace('Counter(', "")
    )
            print("_" * 12)
            continue
        if key == "loot_bag":
            print("Loot!:")
            loot_list=list()
            for each in value:
                loot_list.append(id_to_item(each))
            loot_str = str(Counter(loot_list))
            print(loot_str
        .replace("}", "")
        .replace("'", "")
        .replace("{", "")
        .replace(")", "")
        .replace('"', "")
        .replace('Counter(', "")
    )
            print("_" * 12)
            #clean up with a counter and id_to_item
            continue
        print(key, value)
        print("_" * 12)
    size = stats["feildsize"]
    size = int(size)
    feild = stats["feild"]
   #  ##|##|##|##|##|##|##|##|##|
    feild_list = feild.split("|")
    #prints header numbers
    for each in range(size):
        print(f"{each+1}  |",end="")
    print("")
    count = 0
    #removes blank end element that caused many errors
    del feild_list[-1]
    #prints the feild in a square (hopfully)
    for each in feild_list:
        each = str(id_to_item(each[0])) + each[1]
        print(each,end="|")
        count = count + 1
        if count >= size:
            count = 0
            print("")
    print("")
    wait()


def get_bag():
    pick = cow(
        "Welcome to your bag, I promise I only rumaged    around here a little.  You can:\n1. View seeds\n2. View Loot\n3. Waste my time by doing nothing.",
        prompt="Option: ",
    )
    match pick.lower():
        case "1" | "1." | "seeds" | "view seeds" | "s":
            view_seeds()
        case "2" | "2." | "loot" | "view loot" | "l":
            view_loot()


def view_seeds():
    clear()
    seeds = stats["seed_bag"]
    #seed_list.remove("")
    new_seeds=""
    for each in seeds:
        new_seeds = new_seeds + str(id_to_item(each))
    seed_count = str(Counter(new_seeds))
    print("_" * 7 + "Seeds" + "_" * 7)  # 19 chars long
    print(seed_count.replace("Counter(", "").replace("}", "").replace("'", "").replace("{", "").replace(")", "").replace('"', ""))
    print("_" * 19)
    pick = wait(prompt="Would you like to:\n1. plant somthing?\n2. Go back? ")
    match pick.lower():
        case "yes" | "y" | "p" | "plant" | "1" | "1.":
            plant(seed_count)


def view_loot():
    clear()
    loot = stats["loot_bag"]
    new_loot=""
    for each in loot:
        new_loot = new_loot + str(id_to_item(each))
    loot_count = str(Counter(new_loot))
    print("_" * 7 + "Loot" + "_" * 7)  # 19 chars long
    print(loot_count.replace("Counter(", "").replace("}", "").replace("'", "").replace("{", "").replace(")", "").replace('"', ""))
    print("_" * 19)
    pick = wait(prompt="Would you like to:\n1. Sell somthing?\n2. Go back? ")
    match pick.lower():
        case "yes" | "y" | "s" | "sell" | "1" | "1.":
            market()



def plant(seed_count):
    if len(seed_count) == 0:
        cow("You have no seeds, dumbass")
        return
    if not "##" in stats["feild"]:
        cow("Your feilds are full its time to sleep and let   them grow!")
        return
    seed_count = seed_count.replace("Counter(", "").replace("}", "\n").replace("'", "").replace("{", "").replace(")", "")
    new_seed_count=""
    for each in seed_count:
        if id_to_item(each,flip=True):
            new_seed_count = new_seed_count + each.replace(each, "["+id_to_item(each,flip=True)+"]"+each)
        else:
            new_seed_count = new_seed_count + each
    plant_crop(cow(
        f"What crop would you like to plant you have the   following:\n {new_seed_count}",
        prompt="Enter the name of a seed to plant that seed: ",
    ))


def plant_crop(crop):
    if not len(crop) == 1:
        return
    split = stats["seed_bag"]
    found = False
    for each in split:
        if crop[0] in each:
            found = True
    if not found:
        cow("Could't find that seed try somthing you own, If I could grow anything I'd grow gold.")
        return
    else:
        cow("Planted for you!") #stats["seed_bag"] = stats["seed_bag"].replace(crop[0],"",1) **********************************
    stats["seed_bag"] = stats["seed_bag"].replace(crop[0],"",1)
    feild = stats["feild"]
    feild = feild.replace("##",crop+crop,1)
    #['1. 🥔 Seeds'],
    stats["seed_bag"] = re.sub(f"\['{crop}\. . Seeds'\],","",stats["seed_bag"],count=1)
    stats["feild"] = feild


def sleep():
    # sleeps resotring HP, growing crops one level, check farmer XP for level up
    #resort HP to max
    stats["hp"] = stats["max_hp"]
    #rolls for combat
    combat_start()
    #grow crops
    update_crops()
    #check for levelup
    if int(stats["exp"]) > int(stats["level"])**2+10:
        stats["exp"]=0
        level_up()
    print("""
     .::""-,                      .::""-.
    /::     \                    /::     \
    \n    |::     |   _..--````--.._   |::     |
    '\:.__ /  .'              '.  \:.__ /
     ||____|.' _..---"````'---. '.||____|
     ||:.  |_.'                `'.||:.  |
     ||:.-'`       .-----.        ';:.  |
     ||/         .'       '.        \.  |
     ||         / '-.   '. \\       |.  |
     ||:.     _| '   \_\_\\/(        \  |
     ||:.\_.-' )     ||   m `\.--._.-""-;
     ||:.(_ . '\ __'// m ^_/ /    '.   _.`.
     ||:.  \__^/` _)```'-...'   _ .-'.'    '-.
     ||:..-'__  .'        '. . '      '.      `'.
     ||:(_.' .`'        _. ' '-.         '.   . ''-._
     ||:. :   '.     .'          '.  . ' ' '.`       '._
     ||:.  :    '. .'     .::""-: .''.        ' .   . ' ':::''-.
     ||:. .'    ..' .    /::     \    '.        . '.    /::     \
     \n     ||:.'    .'      '. |::     |    _.:---""---.._'   |::     |
     ||.      :          '\:.__ /   .'    -.  .-    '.   \:.__ /
     ||:     : '.       . ||____|_.'    .--.  .--.    '._||____|
     ||:'.___:   '.   .'  ||:.  |      (    \/    )      ||:.  |
     ||:___| \     '. :   ||:.  |       '-.    .-'       ||:.  |
     [[____]  '.     '.-._||:.  |      __  '..'  __      ||:.  |
                '.    :   ||:.  |     (__\ (\/) /__)     ||:.  |
                  '.  :   ||:.  |        `  \/  `        ||:.  |
                    '-:   ||:.  |           ()           ||:.  |
                       '._||:.  |________________________||:.  |
                      9003||:___|'-.-'-.-'-.-'-.-'-.-'-.-||:___|
                          [[____]                        [[____]
    """)
    input("Sleep tight!")

def update_crops():
    feild = stats["feild"]
    feild_list = feild.split("|")
    for count, each in enumerate(feild_list):
        try:
            new = int(each[1])-1
            each = each[0] + str(new)
            feild_list[count] = each
        except (IndexError, ValueError):
            pass
    del feild_list[-1]

    stats["feild"]="|".join(feild_list)+"|"


def level_up():
    cow("Hooray you leveled up! All of your stats have    gone up by one.  Watch out as you gain more        powerful so do your foes.")
    stats["level"]= str(int(stats["level"])+1)
    #max_hp
    stats["max_hp"] = int(stats["max_hp"])+5
    #str
    stats["str"] = int(stats["str"])+1
    #def
    stats["def"] = int(stats["def"])+1
    #feild feild + (newFS*newFS - oldFS*oldFS)
    stats["feild"] = stats["feild"] + "##|"*((1+int(stats["feildsize"]))**2 - int(stats["feildsize"])**2)
    #feildsize +1
    stats["feildsize"] = int(stats["feildsize"])+1
    #corrects hp to Max
    stats["hp"] = stats["max_hp"]

def harvest():
    feild_list = stats["feild"].split("|")
    del feild_list[-1]
    harvest_list =list()
    for count, each in enumerate(feild_list):
        if each[1] == "-":
            each = each[0]+"0"
        try:
            if int(each[1]) == 0:
                harvest_list.append(id_to_item(each[0]))
                feild_list[count] = "##|"
        except ValueError:
            pass
    #add FL+"|" to S[F]
    stats["feild"] = "".join(feild_list)
    #print HL
    if len(harvest_list) == 0:
        cow("I dug up some worms but I ate them.  Try sleeping to grow crops")
    else:
        cow(f"You harvested the following: {harvest_list}")
        for count, each in enumerate(harvest_list):
            harvest_list[count] = id_to_item(each[0],flip=True)

        stats["loot_bag"] = stats["loot_bag"] + "".join(harvest_list[0])+""

    #add HL to S[loot_bag]

def id_to_item(id,flip=False):
    if not flip:
        match str(id):
            case "#":
                return "🚜"
            case "1":
                return "🥔"
            case "2":
                return "🥦"
            case "3":
                return "🌽"
            case "4":
                return "🧄"
            case "5":
                return "🥓"
            case "6":
                return "🍌"
            case "7":
                return "🍎"
            case "8":
                return "🥝"
            case "9":
                return "🌰"
    else:
        match str(id):
            case "🚜":
                return "#"
            case "🥔":
                return "1"
            case "🥦":
                return "2"
            case "🌽":
                return "3"
            case "🧄":
                return "4"
            case "🥓":
                return "5"
            case "🍌":
                return "6"
            case "🍎":
                return "7"
            case "🥝":
                return "8"
            case "🌰":
                return "9"
    return False

def combat_start():
    cow(get_combat_prompt())
    minNum = 1
    maxNum = 5 * int(stats["level"])
    MobHp = random.randint(minNum,maxNum)
    while True:
        MobAttk = random.randint(minNum,maxNum)
        MobDef = random.randint(minNum,maxNum)
        MobExp = random.randint(minNum,maxNum)

        pick = cow("You can: \n1. Punch (High accuracy low dmg)\n2. Kick (low accuracy high dmg)\n3. Flee (lose some gold but you won't die tonight",prompt="Option: ")
        match pick:
            case "1":
                MobHp = punch(MobAttk,MobDef,MobHp)
                if MobHp <= 0:
                    cow("Well done you defeated them unwelcome guest.  You really should invest in a better lock.")
                    stats["exp"] = int(stats["exp"]) + MobExp
                    break
            case "2":
                MobHp = kick(MobAttk,MobDef,MobHp)
                if MobHp <= 0:
                    stats["exp"] = int(stats["exp"]) + MobExp
                    cow("Well done you defeated them unwelcome guest.  You really should invest in a better lock.")
                    break
            case "3":
                flee()
                break
        if int(stats["hp"]) <= 0:
            death()
def flee():
    print("""
                        ,////,
                        /// 6|
                        //  _|
                       _/_,-'
                  _.-/'/   \\   ,/;,
               ,-' /'  \\_   \\ / _/
               `\\ /     _/\\  ` /
                 |     /,  `\\_/
                 |     \\'
     /\\_        /`      /\\
   /' /_``--.__/\\  `,. /  \\
  |_/`  `-._     `\\/  `\\   `.
            `-.__/'     `\\   |
                          `\\  \\
                            `\\ \\
                              \\_\\__
                               \\___)

""")
    lost = int(int(stats["gold"]) * .20)
    stats["gold"] = int(int(stats["gold"]) * .80)
    input(f"You run away and lost about {lost} gold!")

def punch(MobAttk,MobDef,MobHp):
    playerAttk= random.randint(1,15) + int(stats["str"]) + int(stats["level"])
    if playerAttk >= MobDef:
        #hit big text
        hitmsg=" _    _ _____ _______ _\n| |  | |_   _|__   __| |\n| |__| | | |    | |  | |\n|  __  | | |    | |  | |\n| |  | |_| |_   | |  |_|\n|_|  |_|_____|  |_|  (_)"
        print(hitmsg)
        input(f"You hit for {stats['str']}")
        MobHp = int(MobHp) - int(stats["str"])
    else:
        MissMsg = " __  __ _         \n|  \\/  (_)        \n| \\  / |_ ___ ___ \n| |\\/| | / __/ __|\n| |  | | \\__ \\__ \\\n|_|  |_|_|___/___/"
        input(MissMsg)
    if MobAttk >= int(stats["def"]):
        #ouch big text
        hitmsg="  ____  _    _  _____ _    _  __     ______  _    _    _____  ____ _______   _    _ _____ _______ _\n / __ \\| |  | |/ ____| |  | | \\ \\   / / __ \\| |  | |  / ____|/ __ \\__   __| | |  | |_   _|__   __| |\n| |  | | |  | | |    | |__| |  \ \\_/ / |  | | |  | | | |  __| |  | | | |    | |__| | | |    | |  | |\n| |  | | |  | | |    |  __  |   \   /| |  | | |  | | | | |_ | |  | | | |    |  __  | | |    | |  | |\n| |__| | |__| | |____| |  | |    | | | |__| | |__| | | |__| | |__| | | |    | |  | |_| |_   | |  |_|\n \\____/ \\____/ \\_____|_|  |_|    |_|  \\____/ \\____/   \\_____|\\____/  |_|    |_|  |_|_____|  |_|  (_)"
        print(hitmsg)
        dmg = int(MobAttk - int(stats["def"])) - int(stats["level"])
        if dmg <= 0:
            dmg = 1
        stats["hp"] = int(stats["hp"]) - int(dmg)
        input("You got hit for " + str(dmg) + " and have " + str(stats["hp"]))

    return MobHp

def kick(MobAttk,MobDef,MobHp):
    playerAttk= random.randint(1,10)+int(stats["str"])+int(stats["level"])
    if playerAttk >= MobDef:
        #hit big text
        hitmsg=" _    _ _____ _______ _\n| |  | |_   _|__   __| |\n| |__| | | |    | |  | |\n|  __  | | |    | |  | |\n| |  | |_| |_   | |  |_|\n|_|  |_|_____|  |_|  (_)"
        print(hitmsg)
        input(f"You hit for {int(stats['str'])+int(stats['level'])}")
        MobHp = int(MobHp) - (int(stats["str"])+int(stats['level']))
    else:
        MissMsg = " __  __ _         \n|  \\/  (_)        \n| \\  / |_ ___ ___ \n| |\\/| | / __/ __|\n| |  | | \\__ \\__ \\\n|_|  |_|_|___/___/"
        input(MissMsg)
    if MobAttk >= int(stats["def"]):
        #ouch big text
        hitmsg="  ____  _    _  _____ _    _  __     ______  _    _    _____  ____ _______   _    _ _____ _______ _\n / __ \\| |  | |/ ____| |  | | \\ \\   / / __ \\| |  | |  / ____|/ __ \\__   __| | |  | |_   _|__   __| |\n| |  | | |  | | |    | |__| |  \ \\_/ / |  | | |  | | | |  __| |  | | | |    | |__| | | |    | |  | |\n| |  | | |  | | |    |  __  |   \   /| |  | | |  | | | | |_ | |  | | | |    |  __  | | |    | |  | |\n| |__| | |__| | |____| |  | |    | | | |__| | |__| | | |__| | |__| | | |    | |  | |_| |_   | |  |_|\n \\____/ \\____/ \\_____|_|  |_|    |_|  \\____/ \\____/   \\_____|\\____/  |_|    |_|  |_|_____|  |_|  (_)"
        print(hitmsg)
        dmg = int(MobAttk - int(stats["def"])) - int(stats["level"])
        if dmg <= 0:
            dmg = 1
        stats["hp"] = int(stats["hp"]) - int(dmg)
        input("You got hit for " + str(dmg) + " and have " + str(stats["hp"]))
    return MobHp

def death():
    global name
    #prints a tombstone with a eulagy
    with open("eulagy.txt", "r") as f:
        listE = f.readlines()
        eulagy = random.choice(listE)
        eulagy = eulagy.replace("{NAME}", name)
        print(name)
        print(f"""
                  ____
                 (    )
                 __)(__
           _____/      \\_____
          |  _     ___   _   ||
          | | \     |   | \  ||
          | |  |    |   |  | ||
          | |_/     |   |_/  ||
          | | \     |   |    ||
          | |  \    |   |    ||
          | |   \. _|_. | .  ||
          |                  ||
               {name}
          |                  ||
  *       | *   **    * **   |**      **
   \))ejm97/.,(//,,..,,\||(,,.,\\,.((//)""")
    print(eulagy)
    sys.exit()


def market():
    clear()
    print("""
                                     _|_
                                  .'.':`.`.
              |                  / /  |  \ \\
             /'\                 ^^^^^^^^^^^
            //|\\           &C   O__u |  u O~
          O ^^^^^           /\_u/\/uuu|uuu\/\\
     &C  /|\_@|   C__@     /)  ( '--------' ,|
     /\_ \@@  | @\/\      /_|   \_\   |    /_|           |
    ( ( `,o--------')      /|   / |  /|\   |\           /'\\
    /__\ /`'  |   <|                        _|_        //|\\
    /|  />   /|\   \`                    .'.':`.`.     ^^^^^
                                        / /  |  \ \    %%|%%  O
                     _|_                ^^^^^^^^^^^   %%%|%%%_/\\
                  .'.':`.`.             C_/  |       '-------'  )
                 / /  |  \ \           <|8888|     {b    |     / \\
                 ^^^^^^^^^^^            88888|    _/\   /|\    |  \\
          ~C          |   O       -----------+----' ,|
          /),\_ O     | \/|\/                |    |/_(
       o /( )  /|\    |   | O  |            /|\   | \\
      (`' )_(  \|'-----------'/\\
      /\  / |   |\    |  _o  /  )
                |/   /|\  (`'  /|
                          />   \ \\
    """)
    while True:
        pick = input("Welcome to the market! Are you here to [1.] Buy! or [2.] Sell! [3.] Leave ")
        match pick.lower():
            case "1"|"1."|"buy"|"buy!":
                buy()
                break
            case "2"|"2."|"sell"|"sell!":
                sell()
                break
            case "3"|"3."|"leave"|"leave!":
                return
def buy():
    clear()
    priceMod = random.randint(1,int(stats["level"]))
    market=f"""
    What would you like to buy? We have the following:
    [1.] 🥔: {priceMod*1} gold per seed
    [2.] 🥦: {priceMod*3} gold per seed
    [3.] 🌽: {priceMod*5} gold per seed
    [4.] 🧄: {priceMod*7} gold per seed
    [5.] 🥓: {priceMod*9} gold per seed
    [6.] 🍌: {priceMod*11} gold per seed
    [7.] 🍎: {priceMod*13} gold per seed
    [8.] 🥝: {priceMod*15} gold per seed
    [9.] 🌰: {priceMod*17} gold per seed
    You have a total of {stats["gold"]}
    You can also always leave by typing anything that is not 1-9
    """

    while True:
        pick = input(market)
        match pick:
            case "1":
                seed = input(f"How many do you want? (🥔: {priceMod*1} gold per seed)")
                price = int(seed) * int(priceMod) * 1
                input(price)
                if price > int(stats["gold"]):
                    input("Get out of here until you have more gold!")
                else:
                    stats["gold"] = int(stats["gold"]) - price
                    stats["seed_bag"] = stats["seed_bag"] + pick * int(seed)
                    input("Enjoy your 🥔 seeds")
            case "2":
                seed = input(f"How many do you want? (🥦: {priceMod*3} gold per seed)")
                price = int(seed) * int(priceMod) * 1
                if price > int(stats["gold"]):
                    input("Get out of here until you have more gold!")
                else:
                    stats["gold"] = int(stats["gold"]) - price
                    stats["seed_bag"] = stats["seed_bag"] + pick * int(seed)
                    input("Enjoy your 🥦 seeds")
            case "3":
                seed = input(f"How many do you want? (🌽: {priceMod*5} gold per seed)")
                price = int(seed) * int(priceMod) * 1
                if price > int(stats["gold"]):
                    input("Get out of here until you have more gold!")
                else:
                    stats["gold"] = int(stats["gold"]) - price
                    stats["seed_bag"] = stats["seed_bag"] + pick * int(seed)
                    input("Enjoy your 🌽 seeds")
            case "4":
                seed = input(f"How many do you want? (🧄: {priceMod*7} gold per seed)")
                price = int(seed) * int(priceMod) * 1
                if price > int(stats["gold"]):
                    input("Get out of here until you have more gold!")
                else:
                    stats["gold"] = int(stats["gold"]) - price
                    stats["seed_bag"] = stats["seed_bag"] + pick * int(seed)
                    input("Enjoy your 🧄 seeds")
            case "5":
                seed = input(f"How many do you want? (🥓: {priceMod*9} gold per seed")
                price = int(seed) * int(priceMod) * 1
                if price > int(stats["gold"]):
                    input("Get out of here until you have more gold!")
                else:
                    stats["gold"] = int(stats["gold"]) - price
                    stats["seed_bag"] = stats["seed_bag"] + pick * int(seed)
                    input("Enjoy your 🥓 seeds")
            case "6":
                seed = input(f"How many do you want? (🍌: {priceMod*11} gold per seed)")
                price = int(seed) * int(priceMod) * 1
                if price > int(stats["gold"]):
                    input("Get out of here until you have more gold!")
                else:
                    stats["gold"] = int(stats["gold"]) - price
                    stats["seed_bag"] = stats["seed_bag"] + pick * int(seed)
                    input("Enjoy your 🍌 seeds")
            case "7":
                seed = input(f"How many do you want? (🍎: {priceMod*13} gold per seed")
                price = int(seed) * int(priceMod) * 1
                if price > int(stats["gold"]):
                    input("Get out of here until you have more gold!")
                else:
                    stats["gold"] = int(stats["gold"]) - price
                    stats["seed_bag"] = stats["seed_bag"] + pick * int(seed)
                    input("Enjoy your 🍎 seeds")
            case "8":
                seed = input(f"How many do you want? (🥝: {priceMod*15} gold per seed)")
                price = int(seed) * int(priceMod) * 15
                if price > int(stats["gold"]):
                    input("Get out of here until you have more gold!")
                else:
                    stats["gold"] = int(stats["gold"]) - price
                    stats["seed_bag"] = stats["seed_bag"] + pick * int(seed)
                    input("Enjoy your 🥝 seeds")
            case "9":
                seed = input(f"How many do you want? (🌰: {priceMod*17} gold per seed)")
                price = int(seed) * int(priceMod) * 17
                if price > int(stats["gold"]):
                    input("Get out of here until you have more gold!")
                else:
                    stats["gold"] = int(stats["gold"]) - price
                    stats["seed_bag"] = stats["seed_bag"] + pick * int(seed)
                    input("Enjoy your 🌰 seeds")
            case _:
                break



def sell():
    while True:
        loot=stats["loot_bag"]
        if len(stats["loot_bag"]) == 0:
            clear()
            cow("I'm hungry and your out of loot to sell lets go  home!")
            return
        else:
            clear()
            pick = random.choice(loot)
            priceMod = random.randint(1,int(stats["level"]))
            print("""
      ***
    *******
   *********
/\* ### ### */\\
|    @ / @    |
\/\    ^    /\/
   \  ===  /
    \_____/
     _|_|_
  *$$$$$$$$$*
                   """)
            print(f"I would like to buy one of your {id_to_item(pick)}, please!  I only have {int(priceMod) * int(pick)} Gold to spend.  I hope that is alright!")
            picks = input(f"""
            [1] Sell {id_to_item(pick)} for {int(priceMod)*int(pick)}
            [2] Pass on the offer and wait for someone new
            [3] Give it away for free
            [4] Pack up shop and head home.
            [Anything else] Sit and star in the great beyound to contemplate life.
            """)
            match picks.lower():
                case "1" | "sell" | "yes":
                    stats['gold'] = int(stats['gold']) + int(priceMod)*int(pick)
                    input(f"Thanks! Here's the gold you now have {stats['gold']} gold in total")
                    stats['loot_bag'] = stats['loot_bag'].replace(pick,"",1)
                case "2" | "pass" | "no":
                    input("Whatever the farmer next door looks like they will sell them cheaper.")
                    pass
                case "3" | "free" | "give":
                    input("Thank you kind farmer this will feed my family.  May you have good luck and all your dreams come true")
                    stats['loot_bag'] = stats['loot_bag'].replace(pick,"",1)
                case "4" | "leave":
                    return
                case _:
                    input("I'm pretty sure you are being robbed but your mind is clear and you know what, you found the real treasure inner peace.")
                    stats['loot_bag'] = stats['loot_bag'].replace(pick,"",1)
                    stats['gold'] = int(int(stats['gold']) * 90)
############################################################Todo Functions#####################
#add items like armor and weapons.

def get_combat_prompt():
    prompt = "You hear, 'I was once an adventurer like you' at your door suddenly a figure bursts in."
    #reads file combat_prompts
    #gets Mob
    mob = get_mob()
    #picks one at random
    return prompt

def get_mob():
    mob = "A bandit"
    #reads a file mobs
    #picks one at random
    #gets a random mod for the Mob
    mob = get_mod_for_mob(mob)
    return mob

def get_mod_for_mob(mob):
    #reads a file called mob_mods
    #picks one at random
    mob = mob.replace("{mob}",mob)
    return mob

##########################################Short Cut functions##################




def wait(prompt=None):
    if not prompt:
        input("Press enter to continue...")
    else:
        print("\n")
        return input(prompt)

def clear():
    print(chr(27) + "[2J")


def cow(words, prompt=""):
    # clears the termanal
    clear()
    cowsay.cow(words)
    if prompt == "":
        return input("Press Enter to continue...")
    return input(prompt)


if __name__ == "__main__":
    main()
