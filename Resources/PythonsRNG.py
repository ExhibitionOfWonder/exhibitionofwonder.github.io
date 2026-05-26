# A game inspired by Sol's RNG. Started developement on 06/04/2024

# Importing important stuffs
import random
import time
import sys

# Resetting the stat when closed(Might delete when making a save-available version)
kismet = 0

been_to_shop = False

first_upgrade_bought = False
second_upgrade_bought = False
third_upgrade_bought = False

# Oh no...
common_probability_unlocked = False
uncommon_probability_unlocked = False
unusual_probability_unlocked = False
rare_probability_unlocked = False
scarce_probability_unlocked = False
barely_probability_unlocked = False
super_probability_unlocked = False
legendary_probability_unlocked = False
ultra_probability_unlocked = False
hyper_probability_unlocked = False
mythic_probability_unlocked = False
improbable_probability_unlocked = False
unthinkable_probability_unlocked = False
impossible_probability_unlocked = False
godly_probability_unlocked = False

# Crossline, A.K.A. Just seperating lines
def crossline():
    print("-------------------------------------------------------------------------------------------------------------")
# Cool rolling effect, inspired by Sol's RNG. Fixed the rigged issue!
def cool_rolling_effect():
    randomized_number_for_coolness = random.random()
    if randomized_number_for_coolness <= 0.5:
        print(list_of_probabilities[0])
    elif randomized_number_for_coolness > 0.5 and randomized_number_for_coolness <= 0.75:
        print(list_of_probabilities[1])
    elif randomized_number_for_coolness > 0.75 and randomized_number_for_coolness <= 0.875:
        print(list_of_probabilities[2])
    elif randomized_number_for_coolness > 0.875 and randomized_number_for_coolness <= 0.9375:
        print(list_of_probabilities[3])
    elif randomized_number_for_coolness > 0.9375 and randomized_number_for_coolness <= 0.96875:
        print(list_of_probabilities[4])
    elif randomized_number_for_coolness > 0.96875 and randomized_number_for_coolness <= 0.984375:
        print(list_of_probabilities[5])
    elif randomized_number_for_coolness > 0.984375 and randomized_number_for_coolness <= 0.9921875:
        print(list_of_probabilities[6])
    elif randomized_number_for_coolness > 0.9921875 and randomized_number_for_coolness <= 0.99609375:
        print(list_of_probabilities[7])
    elif randomized_number_for_coolness > 0.99609375 and randomized_number_for_coolness <= 0.998046875:
        print(list_of_probabilities[8])
    elif randomized_number_for_coolness > 0.998046875 and randomized_number_for_coolness <= 0.9990234375:
        print(list_of_probabilities[9])
    elif randomized_number_for_coolness > 0.9990234375 and randomized_number_for_coolness <= 0.99951171875:
        print(list_of_probabilities[10])
    elif randomized_number_for_coolness > 0.99951171875 and randomized_number_for_coolness <= 0.999755859375:
        print(list_of_probabilities[11])
    elif randomized_number_for_coolness > 0.999755859375 and randomized_number_for_coolness <= 0.9998779296875:
        print(list_of_probabilities[12])
    elif randomized_number_for_coolness == 0.999999999999:
        print(list_of_probabilities[13])
    elif randomized_number_for_coolness == 1:
        print(list_of_probabilities[14])

# List of Probabilities(There's many!)
list_of_probabilities = ["Common", "Uncommon", "Unusual", "Rare", "Scarce", "Barely", "Super", "Legendary", "Ultra", "Hyper", "Mythic", "Improbable", "Unthinkable", "Impossible", "Godly"]
# Checking if a player has enough Kismets to buy an upgrade
def checking_kismets():
    price_for_one = 100
    price_for_two = 50
    price_for_three = 150
    global kismet, first_upgrade_bought, second_upgrade_bought, third_upgrade_bought
    buying_upgrade = input("Please insert in the corresponding number of the upgrade you wish to buy(Insert 0 to exit): ").lower().strip()
    if int(buying_upgrade) == 1:
        if kismet < price_for_one:
            print("You do not have enough Kismets.")
            kismets_needed = str(price_for_one - kismet)
            print("You need to collect " + kismets_needed + " more Kismets.")
            checking_kismets()
        else:
            print("Bought!")
            first_upgrade_bought = True
            checking_kismets()
    elif int(buying_upgrade) == 2:
            if kismet < price_for_two:
                print("You do not have enough Kismets.")
                kismets_needed = str(price_for_two - kismet)
                print("You need to collect " + kismets_needed + " more Kismets.")
                checking_kismets()
            else:
                print("Bought!")
                second_upgrade_bought = True
                checking_kismets()
    elif int(buying_upgrade) == 3:
            if kismet < price_for_three:
                print("You do not have enough Kismets.")
                kismets_needed = str(price_for_three - kismet)
                print("You need to collect " + kismets_needed + " more Kismets.")
                checking_kismets()
            else:
                print("Bought!")
                third_upgrade_bought = True
                checking_kismets()
    elif int(buying_upgrade) == 0:
        crossline()
        print("Exitted.")
        crossline()
        menu()
    else:
        print("The upgrade is not recognized.")
        checking_kismets()
# The code behind rolling
def rolling():
    global list_of_probabilities, cool_rolling_effect, rare_probability_found
    global common_probability_unlocked, uncommon_probability_unlocked, unusual_probability_unlocked, rare_probability_unlocked
    global scarce_probability_unlocked, barely_probability_unlocked, super_probability_unlocked, legendary_probability_unlocked
    global ultra_probability_unlocked, hyper_probability_unlocked, mythic_probability_unlocked, improbable_probability_unlocked 
    global unthinkable_probability_unlocked, impossible_probability_unlocked, godly_probability_unlocked
    # Giving effects when third upgrade is bought
    if third_upgrade_bought == False:
        # Generating random numbers, from 0.000000000000 to 1
        randomized_number = random.random()
    else:
        randomized_number = random.uniform(0.500000000000, 1)
    crossline()
    # Giving effects when second upgrade is bought
    if second_upgrade_bought == False:
        cool_rolling_effect()
        time.sleep(0.1)
        cool_rolling_effect()
        time.sleep(0.1)
        cool_rolling_effect()
        time.sleep(0.1)
        cool_rolling_effect()
        time.sleep(0.1)
        cool_rolling_effect()
        time.sleep(0.1)
        cool_rolling_effect()
        time.sleep(0.2)
        cool_rolling_effect()
        time.sleep(0.3)
        cool_rolling_effect()
        time.sleep(0.5)
        cool_rolling_effect()
        time.sleep(0.75)
    else:
        cool_rolling_effect()
        time.sleep(0.05)
        cool_rolling_effect()
        time.sleep(0.05)
        cool_rolling_effect()
        time.sleep(0.05)
        cool_rolling_effect()
        time.sleep(0.05)
        cool_rolling_effect()
        time.sleep(0.05)
        cool_rolling_effect()
        time.sleep(0.1)
        cool_rolling_effect()
        time.sleep(0.15)
        cool_rolling_effect()
        time.sleep(0.25)
        cool_rolling_effect()
        time.sleep(0.375)
    crossline()
    # The entire random generating system. Gosh this took long
    if randomized_number <= 0.5:
        print("You got a(n) " + list_of_probabilities[0] + "!")
        common_probability_unlocked = True
    elif randomized_number > 0.5 and randomized_number <= 0.75:
        print("You got a(n) " + list_of_probabilities[1] + "!")
        uncommon_probability_unlocked = True
    elif randomized_number > 0.75 and randomized_number <= 0.875:
        print("You got a(n) " + list_of_probabilities[2] + "!")
        unusual_probability_unlocked = True
    elif randomized_number > 0.875 and randomized_number <= 0.9375:
        print("You got a(n) " + list_of_probabilities[3] + "!")
        rare_probability_unlocked = True
    elif randomized_number > 0.9375 and randomized_number <= 0.96875:
        print("You got a(n) " + list_of_probabilities[4] + "!")
        scarce_probability_unlocked = True
    elif randomized_number > 0.96875 and randomized_number <= 0.984375:
        rare_probability_found()
        print("You got a(n) " + list_of_probabilities[5] + "!!!")
        barely_probability_unlocked = True
    elif randomized_number > 0.984375 and randomized_number <= 0.9921875:
        rare_probability_found()
        print("You got a(n) " + list_of_probabilities[6] + "!!!")
        super_probability_unlocked = True
    elif randomized_number > 0.9921875 and randomized_number <= 0.99609375:
        rare_probability_found()
        print("You got a(n) " + list_of_probabilities[7] + "!!!")
        legendary_probability_unlocked = True
    elif randomized_number > 0.99609375 and randomized_number <= 0.998046875:
        rare_probability_found()
        print("You got a(n) " + list_of_probabilities[8] + "!!!")
        ultra_probability_unlocked = True
    elif randomized_number > 0.998046875 and randomized_number <= 0.9990234375:
        rare_probability_found()
        print("You got a(n) " + list_of_probabilities[9] + "!!!")
        hyper_probability_unlocked = True
    elif randomized_number > 0.9990234375 and randomized_number <= 0.99951171875:
        rare_probability_found()
        print("You got a(n) " + list_of_probabilities[10] + "!!!")
        mythic_probability_unlocked = True
    elif randomized_number > 0.99951171875 and randomized_number <= 0.999755859375:
        rare_probability_found()
        print("You got a(n) " + list_of_probabilities[11] + "!!!")
        improbable_probability_unlocked = True
    elif randomized_number > 0.999755859375 and randomized_number <= 0.9998779296875:
        rare_probability_found()
        print("You got a(n) " + list_of_probabilities[12] + "!!!")
        unthinkable_probability_unlocked = True
    elif randomized_number == 0.999999999999:
        rare_probability_found()
        print("Wow. Just wow. You got a(n) " + list_of_probabilities[13] + ". Absolutely crazy.")
        impossible_probability_unlocked = True
    elif randomized_number == 1:
        rare_probability_found()
        rare_probability_found()
        rare_probability_found()
        print("""Congratulations.
              You have officially gotten the probability... Godly.
              Words cannot describe how rare this is.
              Well, it probably can.
              1 in 100000000000.
              You may now rest as the god of this game.""")
        godly_probability_unlocked = True
    # Continuing the effect from the third upgrade
    if third_upgrade_bought == False:
        randomized_number = random.random()
    else:
        randomized_number = random.uniform(0.500000000000, 1)
    kismet_earn()
    crossline()
    # Asking if roll again or exit
    exit_or_restart_rolling = input("Press enter to roll again. Type 'Exit' to exit. ").lower().strip()
    if exit_or_restart_rolling == "":
        rolling()
    elif exit_or_restart_rolling == "exit":
        menu()
    else:
        print("The command is not recognized.")
        print("I guess I'll send you to the menu.")
        menu()

# Defining how to earn Kismets every roll
def kismet_earn():
    global kismet
    global first_upgrade_bought
    if first_upgrade_bought == False:
        kismet = kismet + 1
        print("You have earned 1 Kismet.")
    else:
        kismet = kismet + 3
        print("You have earned 3 Kismets.")
# Cool effect, again, inspired by Sol's RNG
def rare_probability_found():
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
def menu():
    global menu_input
    global rolling, checking_kismets, been_to_shop, kismet

    crossline()

    menu_input = input("Press enter to continue, and 'Info' for information and commands. ").lower().strip()

    if menu_input == "":
        rolling()
    elif menu_input == "info":
        crossline()
        print("""This game, as you expected, is inspired by Sol's RNG from Roblox.
I made this game to practice Python and randomizer.
There are currently 15 Probabilities.
Think of Probabilities as Auras from Sol's RNG.
There will be more updates, so enjoy.
Good Luck.

Commands:
(Insert in 'Exit" in all of the commands to exit)
Shop: Opens Shop
Update Logs: Shows new update feature
Yeah that's it so far... Gonna add more""")
        menu()
    elif menu_input == "shop":
        crossline()
        if been_to_shop == False:
            print("Seems like you've never been to the shop before.")
            print("Basically, you can buy upgrades here.")
            print("Use your 'Kismet' (Basically currencies for this game) to buy upgrades.")
            print("Kismet means 'fate, destiny, or predetermined fortune'. Fits the game's theme.")
            print("By any means now, go ahead.")
            input("Press enter to continue. ")
            crossline()
            been_to_shop = True
        print("You currently have " + str(kismet) + " Kismets.")
        print("""Current upgrades available:
          
1. More Kismets per roll
Price: 100 Kismets
          
2. Faster roll
Price: 50 Kismets
          
3. Increased luck
Price: 150 Kismets
          
4. Unlock more upgrades
Price: Coming soon""")
        
        checking_kismets()
    elif menu_input == "exit":
        are_you_sure = input("Are you sure? You will lose all your data!(Y/N) ").lower().strip()
        if are_you_sure == "y" or are_you_sure == "yes":
            sys.exit()
        elif are_you_sure == "n" or are_you_sure == "no":
            menu()
        else:
            print("C'mon. Just pick one.")
            menu()
    elif menu_input == "update logs" or menu_input == "update log":
        crossline()
        print("""06/06/2024 Update
As known as...
VER. ALPHA!
              Actually operating game!
              New introduction message!
              Added Update Logs!
              Fixed the rigged effect!
              YOU CAN EXIT FROM FEATURES!!!
              Help from ChatGPT!
              Fixed... Literally everything!
              Many more!""")
        input("Press enter to exit. ")
        menu()
    else:
        print("The command is not recognized.")

crossline()
crossline()
crossline()

time.sleep(1)

print("2 Full days of grinding.")

time.sleep(1)

print("Unnecesarry errors.")

time.sleep(1)

print("300+ lines of coding.")

time.sleep(1)

print("I present to you...")

time.sleep(1)

print("Python's RNG. Enjoy.")

time.sleep(1)
menu()