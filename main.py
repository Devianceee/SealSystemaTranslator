# This is very badly coded and rushed i just thought it would be fun to make

def ggsToWord(inputString):
    inputString = inputString.strip()

    systemaDict = {"gg gg": " ", "gg Gg": ".", "gg GG": ",", "gg ggs": "?", "gg Ggs": "!", "gg GGs": ";",
                    "Gg gg": "A", "Gg Gg": "B", "Gg GG": "C", "Gg ggs": "D", "Gg Ggs": "E", "Gg GGs": "F", 
                    "GG gg": "G", "GG Gg": "H", "GG GG": "I", "GG ggs": "K", "GG Ggs": "L", "GG GGs": "M",
                    "ggs gg": "N", "ggs Gg": "O", "ggs GG": "P", "ggs ggs": "Q", "ggs Ggs": "R", "ggs GGs": "S",
                    "Ggs gg": "T", "Ggs Gg": "U", "Ggs GG": "V", "Ggs ggs": "W", "Ggs Ggs": "Y", "Ggs GGS": "Z", 
                    "GGs gg": ":clown:", "GGs Gg": ":mech:", "GGs GG": ":hisui:", "GGs ggs": ":akiha1:", "GGs Ggs": ":akiha2:", "GGs GGs": ":same:"}

    return systemaDict[inputString]
            
print ("Seal Systema Translator by Deviance\n")

print ("Opening text file...")

overallMessage = ""
ggsLetter = ""
counter = 0

with open('ggs.txt', 'r') as file:

    for line in file:

        for word in line.split():
            ggsLetter += word + " "
            counter += 1
            if counter == 2:
                counter = 0
                overallMessage += ggsToWord(ggsLetter)
                ggsLetter = ""

print(overallMessage)
input("Press enter to exit...")
