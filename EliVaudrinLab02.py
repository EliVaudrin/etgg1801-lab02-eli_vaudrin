#Etgg 1801
#Eli Vaudrin
#Lab02 - Expressions
#Date: 9/9/2020

#Legend of Zelda Triforce Symbol

print("            _\n           / \\\\")
print("          /   \\\\ \r\n         /     \\\\")
print("        /       \\\\ \n       /_________\\\\")
print("      /\\         /\\\\ \r\n     /  \\       /  \\\\")
print("    /    \\     /    \\\\ \n   /      \\   /      \\\\")
print("  /________\\_/________\\\\ \n")

#Skull
print("                           _________________ \r\n                       ___/:::::::::::::::::\\___ \n"
      "                ______/::::                     \\______ \r\n             __/::::                                   \\__ \n"
      "            /::::                                         \\ \r\n           /:::                                            \\ \n"
      "          |:::::   :X                      :::              | \r\n          |:::::::: X                     :::               | \n"
      "          |::::::    X                    :                 | \r\n          |:::::      X:::                      :::::       | \n"
      "           \\:::::   XXXXXXX:                   XXXXXXX:    / \r\n           |::    XXXXXXXXX:                 XXXXXXXXX:    | \n"
      "           |::    XXXXXXXXXX:               XXXXXXXXXX::   | \r\n           |::     XXXXXXXX:       XXX       XXXXXXXX:::   | \n"
      "           |         XXXX:       XX   XX       XXXX::::    | \r\n            \\                   XX     XX                 / \n"
      "             \\___              XXX     XXX            ___/ \r\n                 \\              XX     XX            / \n"
      "                  |                                 | \r\n                   \\_______________________________/ \n"
      "                    | |  |   |   |   |   |   |  | |  \r\n                    |_|__|___|___|___|___|___|__|_| \n")

#Interactive Health Bar
barLength =len("[::::::::::::::::::::::::::::::::::::::::::::::::]")
currentHealth= int(input("Input your current health from 1-50:"))
maxHealth = int(input("Input your max health from 1-50:"))
print(" _________________________________________________ \n"
      "|::::::::::::::::::::",currentHealth, "/",maxHealth,"::::::::::::::::::::| \n"
      " -------------------------------------------------")

print(input("Press enter to continue."))

#Conversation Bot
name = input("What is your name?")
print("Hello there, " + name,".")
game= input("What is your favorite game?")
print("Wow " + game, "sounds like a fun game!")
hobby = input("What do you like to do in your freetime?")
print(hobby,"sounds like a fun thing to do in your freetime.")
show = input("What is your favorite tv show")
print(show,"sounds like a cool tv show.")
actor = input("Who is your favorite actor?")
print(actor,"must be a talented actor")
music = input("What is your favorite song?")
print(music,"sounds like a good song to listen to.")
print("Goodbye now " + name, ",I hope to talk again with you soon.")
input("Press enter to close")