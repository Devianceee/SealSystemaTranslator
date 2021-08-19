# This is very badly coded and rushed i just thought it would be fun to make

def ggsToWord(inputString):
    inputString = inputString.strip()

    if (inputString == "gg gg"):
        return " "

    elif (inputString == "gg Gg"):
        return "."
            
    elif (inputString == "gg GG"):
        return ","
            
    elif (inputString == "gg ggs"):
        return "?"
            
    elif (inputString == "gg Ggs"):
        return "!"
            
    elif (inputString == "gg GGs"):
        return ";"
            
    elif (inputString == "Gg gg"):
        return "A"
            
    elif (inputString == "Gg Gg"):
        return "B"
            
    elif (inputString == "Gg GG"):
        return "C"
            
    elif (inputString == "Gg ggs"):
        return "D"
            
    elif (inputString == "Gg Ggs"):
        return "E"
            
    elif (inputString == "Gg GGs"):
        return "F"
            
    elif (inputString == "GG gg"):
        return "G"
            
    elif (inputString == "GG Gg"):
        return "H"
            
    elif (inputString == "GG GG"):
        return "I"
            
    elif (inputString == "GG ggs"):
        return "K"
            
    elif (inputString == "GG Ggs"):
        return "L"
            
    elif (inputString == "GG GGs"):
        return "M"
            
    elif (inputString == "ggs gg"):
        return "N"

    elif (inputString == "ggs Gg"):
        return "O"
            
    elif (inputString == "ggs GG"):
        return "P"
            
    elif (inputString == "ggs ggs"):
        return "Q"
            
    elif (inputString == "ggs Ggs"):
        return "R"
            
    elif (inputString == "ggs GGs"):
        return "S"
            
    elif (inputString == "Ggs gg"):
        return "T"
            
    elif (inputString == "Ggs Gg"):
        return "U"
            
    elif (inputString == "Ggs GG"):
        return "V"
            
    elif (inputString == "Ggs ggs"):
        return "W"
            
    elif (inputString == "Ggs Ggs"):
        return "Y"

    elif (inputString == "Ggs GGS"):
        return "Z"
        
    elif (inputString == "GGs gg"):
        return ":clown:"
        
    elif (inputString == "GGs Gg"):
        return ":mech:"
        
    elif (inputString == "GGs GG"):
        return ":hisui:"
        
    elif (inputString == "GGs ggs"):
        return ":akiha1:"
            
    elif (inputString == "GGs Ggs"):
        return ":akiha2:"
            
    elif (inputString == "GGs GGs"):
        #print(":same:")
        return ":same:"


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
